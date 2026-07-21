# 📚 Indian Penal Code (IPC) Question-Answering System
An Advanced RAG (Retrieval-Augmented Generation) pipeline built with LangChain and Pinecone to query Indian IPC sections and crime details.
## 💡 What is This Project?
Large Language Models (LLMs) like GPT-4 are powerful, but they have key limitations:
• They are limited to their training cutoff date (e.g., they don't know  events like new sections that added yesterday).
• They lack specialized or private data, such as complete legal codes or internal company HR policies, or private documents.
Retrieval-Augmented Generation (RAG) solves this! By storing legal documents inside Pinecone (a vector database), this system lets an LLM pull real-time, accurate context from the Indian Penal Code before generating an answer.
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