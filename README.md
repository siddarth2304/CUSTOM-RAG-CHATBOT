

````markdown
# InsightBot — Custom RAG Chatbot

A high-performance Retrieval-Augmented Generation (RAG) chatbot built from scratch using Python and the Gemini API.  
It answers questions from uploaded documents (PDF/DOCX) with full control over embeddings, retrieval, and generation.

---

## Project Overview

InsightBot demonstrates a low-level understanding of RAG internals.  
Unlike high-level frameworks such as LangChain, this project emphasizes:

- Direct control over document ingestion, chunking, and embedding  
- FAISS vector indexing for fast retrieval  
- GPU acceleration for embeddings and LLM inference  
- Gemini API (GPT-5) integration for generation  

This showcases the ability to build enterprise-grade AI systems from scratch.

---

## Features

- Upload multiple PDF/DOCX files and generate embeddings automatically  
- Configurable chunking with overlap control  
- FAISS-based vector search for fast and relevant retrieval  
- Gemini-powered generation for contextual answers  
- Multi-document retrieval support  
- GPU acceleration for embeddings and inference  
- Ready for Flask-based web deployment  

---

## Technical Stack

| Layer                       | Technology                     |
|-----------------------------|--------------------------------|
| Document Ingestion & Parsing | PyMuPDF, python-docx           |
| Chunking                    | Custom text chunker (overlap control) |
| Embeddings                  | Custom GPU-accelerated pipeline |
| Vector Database             | FAISS                          |
| LLM Generation              | Gemini API (GPT-5)             |
| Backend API                 | Python, Flask                  |
| Deployment                  | Vercel / Render / Fly.io (planned) |

---

## Low-Level Insights

- Custom Chunking & Embeddings → Fine-grained control over chunk size, overlap, and embedding dimensionality ensures optimal retrieval performance.  
- FAISS Index Management → Direct control of index creation, updating, and querying enables fast and accurate vector search.  
- Gemini API Integration → Direct calls provide full control of prompts and parameters.  
- GPU Optimization → Enables low-latency processing for large documents using CUDA.

---

## LangChain vs Custom RAG (InsightBot)

| Feature             | LangChain (High-level) | InsightBot (Custom, Low-level) |
|----------------------|-------------------------|--------------------------------|
| Abstraction Level    | High                   | Low, full control              |
| Vector Store         | Multiple backends      | Direct FAISS control           |
| LLM Integration      | Wrappers               | Direct Gemini API calls        |
| Chunking             | Predefined utilities   | Custom, configurable logic     |
| Deployment           | Flexible (abstracted)  | Flask API for live uploads     |
| Optimization         | Defaults only          | Manual GPU optimization        |
| Debugging            | Abstracted             | Transparent pipeline           |

**Takeaway:** InsightBot highlights hands-on expertise in building RAG from scratch and optimizing every component.

---

## Example Usage

```bash
# Step 1: Generate embeddings from documents
PYTHONPATH=. python backend/embeddings/embedder.py

# Step 2: Query the RAG chatbot
PYTHONPATH=. python rag_query.py
````

---

With InsightBot, you get full transparency, low-level control, and enterprise-grade performance in your RAG pipeline.

---


```
