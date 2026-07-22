import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_community.tools import DuckDuckGoSearchRun
import streamlit as st
from ddgs import DDGS
from langchain_core.tools import tool

# 1. Load Environment Variables
load_dotenv(override=True)

# 2. Configure Streamlit Page Layout
st.set_page_config(
    page_title="IPC Legal AI Assistant",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("⚖️ Indian Penal Code (IPC) AI Assistant")
st.caption(
    "Query Indian Penal Code sections and offenses with document-grounded answers."
)

# 3. Initialize Model and Runnable Chain
model = ChatOpenRouter(model=os.environ.get("MODEL", "openai/gpt-4o-mini"))

system_prompt_text = """You are a precise, document-grounded AI assistant. Your sole purpose is to answer the user's question using ONLY the provided document context.

### CORE GROUNDING RULES:
1. Zero External Knowledge: You must operate ONLY on the information explicitly contained within the provided context. Do NOT use your prior knowledge, general training data, or outside assumptions.
2. Zero Inferences: Do NOT assume, extrapolate, speculate, or deduce facts that are not directly stated in the context.
3. Strict Fallback: If the exact information needed to answer the query is missing, incomplete, or ambiguous in the context, you MUST output EXACTLY: "I cannot find this information in the provided document."

### CONTEXT:
{context}"""

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt_text),
        ("human", "{input}"),
    ]
)

chain = prompt | model

# Simulated context (In production, replace with Pinecone retrieval)
retrieved_context = (
    "IPC Section 378 defines theft as moving movable property out of "
    "possession without consent with dishonest intention."
)

# 4. Initialize Chat History in Streamlit Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize DuckDuckGo tool
search_tool = DuckDuckGoSearchRun()

with st.sidebar:
    st.header("🔍 Quick web search(not IPC)")
    with st.form("sidebar_search_form"):
        duckduckgo_search = st.text_input(
            "Search widget",
            key="placeholder",
        )
        search_submitted = st.form_submit_button("Search Web")
    # Perform search and render results
    if search_submitted and duckduckgo_search.strip():
        with st.spinner("Searching..."):
            try:
                # Execute DuckDuckGo query via LangChain
                results = search_tool.invoke(duckduckgo_search)
                search_results = st.text(
                    results
                )
            except Exception as e:
                st.error(f"Search failed: {e}")

# Helper Generator Function for Streamlit Streaming
def generate_response(user_input):
    stream = chain.stream({"context": retrieved_context, "input": user_input})
    for chunk in stream:
        yield chunk.content


# 6. Chat Input & Processing Loop
if user_prompt := st.chat_input("Ask a question about the Indian Penal Code..."):
    # Display human query
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Stream AI response using st.write_stream
    with st.chat_message("assistant"):
        response = st.write_stream(generate_response(user_prompt))

    # Append complete response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )