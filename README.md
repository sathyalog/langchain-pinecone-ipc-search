# 📚 Indian Penal Code (IPC) Question-Answering System
An Advanced RAG (Retrieval-Augmented Generation) pipeline built with LangChain and Pinecone to query Indian IPC sections and crime details.
## 💡 What is This Project?
Large Language Models (LLMs) like GPT-4 are powerful, but they have key limitations:
• They are limited to their training cutoff date (e.g., they don't know  events like new sections that added yesterday).
• They lack specialized or private data, such as complete legal codes or internal company HR policies, or private documents.
Retrieval-Augmented Generation (RAG) solves this! By storing legal documents inside Pinecone (a vector database), this system lets an LLM pull real-time, accurate context from the Indian Penal Code before generating an answer.

🚀 Getting Started
Follow these steps to set up and run the project locally using uv.
1. Prerequisites & Installation
If you don't have uv installed, install it using one of the following methods:
####  macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

####  Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

#### Or via pip
`pip install uv`

#### Sync environment
`uv sync`

#### 🛠️ Key Technologies Used
• LangChain: The framework used to connect the LLM with external data and structure prompt workflows.
• Pinecone: A vector database used to store and quickly search document embeddings.
• OpenAI / OpenRouter: The LLM provider generating precise, grounded answers based only on retrieved text.
🔍 How It Works
1. Load Data: Indian Penal Code documents (PDFs or CSVs) are loaded into the system. For this project, we are adding IPC_186045.pdf inside assets folder for reference.
2. Chunk & Embed: The text is split into small section chunks and converted into mathematical representations (vector embeddings).
3. Store in Pinecone: Embeddings are indexed in Pinecone for ultra-fast similarity search.
4. Query & Retrieve: When a user asks a question (e.g., "What is the punishment for extortion?"), Pinecone fetches the exact relevant IPC section.
5. Generate Response: LangChain passes the retrieved section into the LLM, which gives a strict, factual answer based strictly on the document.
#### 🧠 LangChain Core Concepts Explained Simply
Concept	Explanation
LLM Wrappers	Interfaces that let python easily communicate with models like OpenAI or OpenRouter.
Prompt Templates	Pre-defined instructions and grounding rules given to the AI to ensure reliable answers.
Vector Store / Indexes	Databases (like Pinecone) that hold and search through your document chunks.
Chains	Workflows that combine components (Prompt + LLM + Vector Search) to perform a task.
Agents	Smart decision-makers that can dynamically call tools or APIs based on user requests.
#### 🚀 Common RAG Use Cases
• Legal AI: Search laws, statutes, or past legal cases.
• Enterprise Search: Query internal company onboarding docs, HR policies, or tech docs.
• Customer Support: Auto-answer customer queries based on product manuals.

Caching - caching is the practice of storing frequently accessed data or results in a temporary, faster storage layer.

Caching optimizes interactions with LLMs by reducing API calls and speeding up applications, resulting in a more efficient user experience.

**InMemoryCache** and **SQLite Caching** are 2 common methods to cache the inputs.
Syntax would be like:
```
from langchain_core.caches import InMemoryCache
from langchain_core.caches import SQLiteCache
set_llm_cache(InMemoryCache())
set_llm_cache(SQLiteCache(database_path=".langchain.db"))
```

Streaming refers to the process of delivering the response in a continuous stream of data instead of sending entire response at once.

#### Prompt templates:
A prompt refers to the input to the model.

Prompt templates are a way to create dynamic prompts for LLMs.

A prompt template takes a piece of text and injects a users input into that piece of text.

In Langchain there are PromptTemplates and ChatPromptTemplates.

use PromptTemplate for managing your prompts with dynamic placeholders. If you are looking for more modern or specialized ways to handle prompts, consider these alternatives depending on your use case:

**ChatPromptTemplate**: If you are working with chat-based models (which is standard for most modern applications), ChatPromptTemplate is the preferred approach. It allows you to structure prompts as a sequence of messages (system, human, ai), providing better control over message roles and context.

**LangChain Hub**: Instead of hardcoding prompt templates in your code, you can use the LangChain Hub to store, version, and manage your prompts. You can pull them programmatically into your application, making them easier to iterate on without changing your source code.
**Runnable Interface**: Ensure you are using the modern LCEL (LangChain Expression Language) syntax by piping your prompt templates into models using the | operator, rather than older chain constructors.

LCEL (LangChain Expression Language) 
```
from langchain_core.prompts import ChatPromptTemplate

# Use ChatPromptTemplate for chat-based models
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# Use the pipe operator (LCEL) to create your chain
chain = prompt | model
```
The **Runnable interface** is a foundational abstraction in LangChain that provides a standardized way to define, compose, and execute components in your LLM applications.

By implementing the Runnable interface, components (like LLMs, prompt templates, retrievers, or custom logic) get access to a consistent set of methods for execution, streaming, and batching. This standard interface is what enables LangChain Expression Language (LCEL) to work, allowing you to easily chain components together using the pipe (|) operator.

Key Features of the Runnable Interface

    **Standard Execution Methods** : Every Runnable component supports core execution methods:
        .invoke(): Execute the component synchronously on a single input.
        .ainvoke(): Asynchronous version of invoke.
        .batch(): Execute the component on a list of inputs in parallel.
        .abatch(): Asynchronous version of batch.
        .stream(): Stream output from the component as it generates.
        .astream(): Asynchronous version of stream.

    **Composition (LCEL)** : The Runnable interface allows you to compose complex pipelines effortlessly. For example, you can pipe a PromptTemplate into an LLM and then into an OutputParser:

    `chain = prompt_template | llm | output_parser`

    Configurable Behavior: You can pass a RunnableConfig (e.g., for tracing, metadata, or execution settings) to these methods to control runtime behavior across your entire chain.

    Extensibility: Most major components in LangChain (LLMs, chat models, prompt templates, retrievers, tools) implement this interface. If you have custom logic you need to integrate, you can easily turn it into a Runnable using decorators like @chain or by inheriting from Runnable.

**Improvements made:**
    1.	Parameters dynamic injection: Pass parameters directly as a dictionary { "context": ..., "input": ... } into chain.stream().
	2.	LangChain Expression Language (LCEL): The expression chain = prompt | model binds prompt formatting and execution into a clean, reusable pipeline.
	3.	No manual SystemMessage / HumanMessage instantiation: ChatPromptTemplate.from_messages automatically builds the appropriate message objects under the hood based on string tuples.

### Langchain tools
Langchain tools are specialized apps for your LLM. They are tiny code modules that allow it to access your information and services. These tools connect your LLM to search engines, databases, API's and many more.

Tools like DuckDuckGo(search the web), Tavily AI, Wikipedia. 