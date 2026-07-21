import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter

load_dotenv(override=True)

# 1. Initialize Model
model = ChatOpenRouter(model=os.environ.get("MODEL", "openai/gpt-4o-mini"))

# 2. Define System Text with Placeholders
system_prompt_text = """You are a precise, document-grounded AI assistant. Your sole purpose is to answer the user's question using ONLY the provided document context.

### CORE GROUNDING RULES:
1. Zero External Knowledge: You must operate ONLY on the information explicitly contained within the provided context. Do NOT use your prior knowledge, general training data, or outside assumptions.
2. Zero Inferences: Do NOT assume, extrapolate, speculate, or deduce facts that are not directly stated in the context. If an answer requires reading between the lines, treat it as unavailable.
3. Strict Fallback: If the exact information needed to answer the query is missing, incomplete, or ambiguous in the context, you MUST output EXACTLY: "I cannot find this information in the provided document." Do not add any extra text or explanations.

### CONTEXT:
{context}"""

# 3. Create ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt_text),
        ("human", "{input}"),
    ]
)

# 4. Construct Runnable Chain using Pipe Operator (|)
# Prompt formatting -> Model execution -> String output parser (optional)
chain = prompt | model

# Dummy context (in full RAG, this will come from Pinecone)
retrieved_context = "IPC Section 378 defines theft as moving movable property out of possession without consent with dishonest intention."

# 5. Interactive Loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["quit", "exit"]:
        break

    print("AI: ", end="", flush=True)

    # Stream output by passing parameters as a dictionary to the runnable chain
    for chunk in chain.stream(
        {"context": retrieved_context, "input": user_input}
    ):
        print(chunk.content, end="", flush=True)

    print()