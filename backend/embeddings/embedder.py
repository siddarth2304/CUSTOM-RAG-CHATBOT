from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

# Load the model (GPU will be used automatically if available)
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(texts):
    return model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)

def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_index(index, filepath="faiss_index.index"):
    faiss.write_index(index, filepath)

def save_metadata(metadata, filepath="metadata.pkl"):
    with open(filepath, "wb") as f:
        pickle.dump(metadata, f)

# Integration test
if __name__ == "__main__":
    from backend.ingestion.parser import load_documents
    from backend.ingestion.chunker import chunk_documents

    print("📥 Loading documents...")
    docs = load_documents("data")

    print("✂️ Chunking...")
    chunks = chunk_documents(docs, max_tokens=200)

    texts = [c["text"] for c in chunks]
    metadata = [{k: c[k] for k in ["filename", "chunk_id"]} for c in chunks]

    print("🧠 Embedding texts...")
    embeddings = embed_text(texts)
    print(f"✅ Generated {len(embeddings)} embeddings of dim {embeddings.shape[1]}")

    print("📦 Creating FAISS index...")
    index = create_faiss_index(embeddings)

    print("💾 Saving index and metadata...")
    save_index(index)
    save_metadata(metadata)

    print("🎉 All done. You’re ready for retrieval.")
