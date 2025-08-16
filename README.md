
---

````markdown
# InsightBot — Custom RAG Chatbot

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![FAISS](https://img.shields.io/badge/FAISS-VectorSearch-orange)](https://github.com/facebookresearch/faiss)
[![Gemini](https://img.shields.io/badge/Gemini-GPT5-red)](https://developers.generativeai.google/)

**A high-performance Retrieval-Augmented Generation (RAG) chatbot built from scratch using Python and Gemini API, designed to answer questions from uploaded documents (PDF/DOCX) with full control over embeddings, retrieval, and generation.**

---

## 🚀 Project Overview

InsightBot is a **custom-built RAG chatbot** that demonstrates **deep understanding of retrieval, embedding, and generation pipelines**. Unlike off-the-shelf solutions like LangChain, this project emphasizes **low-level control and enterprise-grade architecture**, allowing:

- Direct management of document ingestion, chunking, and embedding
- Custom FAISS vector indexing
- Dynamic query retrieval and generation
- Full GPU acceleration for embeddings and LLM inference

---

## 📂 Features

- Upload multiple PDFs/DOCX and automatically generate embeddings  
- Chunk documents with configurable size and overlap  
- FAISS-based vector search for high-speed retrieval  
- Gemini-powered generation (GPT-5) for coherent, contextual answers  
- Multi-document retrieval and query handling  
- GPU acceleration for embeddings and LLM inference  
- Easy-to-adapt Flask API for web deployment  

---

## ⚙️ Technical Stack

| Layer | Technology |
|-------|------------|
| Document Ingestion & Parsing | PyMuPDF, python-docx |
| Chunking | Custom text chunker with overlap control |
| Embeddings | Custom embeddings pipeline with GPU support |
| Vector Database | FAISS (local vector store) |
| LLM Generation | Gemini API (GPT-5) |
| Backend API | Python, Flask |
| Deployment | Vercel / Render / Fly.io (planned) |

---

## 🧠 Low-Level Insights

- **Custom Chunking & Embeddings:** Fine-grained control over chunk size, overlap, and embedding dimensionality ensures **optimal retrieval performance**.  
- **FAISS Index Management:** Direct control over index creation, updating, and querying ensures **fast vector search** without hidden layers.  
- **Generator Integration:** Direct Gemini API calls allow **full control of prompts and LLM parameters**.  
- **GPU Optimization:** Low-latency processing for large documents, fully leveraging CUDA.  

---

## 🔍 LangChain vs Custom RAG (InsightBot)

| Feature | LangChain | InsightBot (Custom) |
|---------|-----------|-------------------|
| Abstraction Level | High-level | Low-level, full control |
| Vector Store | Supports multiple backends | Direct FAISS control |
| LLM Integration | Standardized wrappers | Direct Gemini API calls |
| Chunking | Predefined utilities | Custom chunking logic, configurable |
| Deployment | Flexible, may need wrappers | Full Flask API for live uploads |
| Optimization | Limited to defaults | GPU acceleration and manual tuning |
| Debugging | Abstracted | Fully transparent pipeline |

**Takeaway:** InsightBot demonstrates **hands-on expertise** in building RAG from scratch and optimizing every component for performance and control.

---

## 📄 Example Usage

```bash
# Generate embeddings from documents
PYTHONPATH=. python backend/embeddings/embedder.py

# Query the RAG chatbot
PYTHONPATH=. python rag_query.py
````

**Sample Query:**

```
Enter your question: What projects have I worked on?
--- Retrieved Chunks ---
Chunk 1: Sahith Siddarth Earlapally, Resume, Technical Skills...
Chunk 2: Distributed Task Queue, Concurrent TCP Server...
Chunk 3: Optimized RAG Chatbot with Vector Search...
--- Generated Answer ---
You have worked on the following projects:
* Concurrent TCP Server from Scratch
* Distributed Task Queue System
* Optimized RAG Chatbot with Vector Search
```

---

## 📈 Key Takeaways 

* Demonstrates **low-level RAG knowledge** and vector search expertise
* Shows **custom pipeline building from scratch**, not relying on pre-built frameworks
* Ability to **debug, optimize, and deploy enterprise-grade AI systems**
* Exposure to **real-world problem-solving**, multi-document retrieval, and GPU optimization

---

## 📌 Next Steps (Planned)

* Web interface for **live PDF/DOCX uploads**
* Real-time query answering with **chunk highlighting** and file references
* Dynamic **FAISS updating** with uploaded documents
* Deployment on **Vercel / Render / Fly.io** with GPU support

---

## 🖼️ Project Flow Diagram

```
[User Uploads PDF/DOCX] --> [Parser & Chunker] --> [Embeddings + FAISS Index] --> [Retriever] --> [Gemini Generator] --> [Answer]
```

---

**Made with ❤️ by Sahith Siddarth**
[LinkedIn](https://linkedin.com/in/earlapally-sahith-siddarth/) | [Portfolio](https://sahithsiddarth.vercel.app/) | [GitHub](https://github.com/siddarth2304)


