# RAG Starter Kit

A beginner-friendly Retrieval-Augmented Generation (RAG) starter repository maintained by **WebPrims**.

This project demonstrates the main building blocks behind a simple RAG system: loading text, splitting it into chunks, creating embeddings, storing vectors, retrieving relevant context, and asking a local language model to answer from that context.

## What you'll learn

- What RAG is and when to use it
- Document loading and chunking
- Embeddings and semantic search
- Vector storage with ChromaDB
- Retrieval of relevant document chunks
- Local LLM generation with Ollama
- How retrieval and generation work together

## Project structure

```text
rag-starter-kit/
├── data/
│   └── sample_knowledge.txt
├── src/
│   ├── chunk_text.py
│   ├── build_index.py
│   ├── search_index.py
│   └── rag_chat.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10+
- Ollama installed and running
- A local chat model such as `llama3.2`
- A local embedding model such as `nomic-embed-text`

Pull the models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

Install Python packages:

```bash
pip install -r requirements.txt
```

## Quick start

### 1. Build the vector index

```bash
python src/build_index.py
```

### 2. Test semantic search

```bash
python src/search_index.py
```

### 3. Start the RAG chatbot

```bash
python src/rag_chat.py
```

Ask questions based on the sample knowledge file. You can later replace that file with your own notes or documents.

## How the pipeline works

```text
Documents
   ↓
Text chunks
   ↓
Embeddings
   ↓
Vector database
   ↓
User question
   ↓
Similarity search
   ↓
Relevant context
   ↓
Local LLM
   ↓
Grounded answer
```

## Learning approach

Start with the small example in this repository. Once you understand the flow, try extending it with PDF loading, metadata, multiple documents, better chunking, reranking, citations, or a web interface.

## Learn AI with WebPrims

WebPrims focuses on practical, project-driven learning in AI, local LLMs, software development, and modern coding workflows.

- AI Edge: https://www.webprims.com/ai-edge
- Official Website: https://www.webprims.com/
- GitHub: https://github.com/webprims

## Note

This starter kit is intentionally simple for learning. Production RAG systems usually need stronger document parsing, metadata handling, evaluation, observability, access controls, and better retrieval strategies.
