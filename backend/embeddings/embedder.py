# backend/embeddings/embedder.py
import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
from backend.ingestion.chunker import chunk_text
from backend.ingestion.parser import load_documents

# -----------------------------
# Settings
# -----------------------------
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DEVICE = "cuda" if True else "cpu"
DATA_DIR = "data"
INDEX_FILE = "faiss_index.index"
METADATA_FILE = "metadata.pkl"

# -----------------------------
# Initialize embedding model
# -----------------------------
embed_model = SentenceTransformer(EMBEDDING_MODEL, device=DEVICE)

# -----------------------------
# Load all documents
# -----------------------------
documents = load_documents(DATA_DIR)
print(f"📥 Loaded {len(documents)} documents from {DATA_DIR}")

# -----------------------------
# Chunk and prepare metadata
# -----------------------------
all_chunks = []
for doc in documents:
    chunks = chunk_text(doc["text"])
    for i, chunk in enumerate(chunks):
        all_chunks.append({
            "text": chunk,            # ✅ actual chunk content
            "filename": doc["filename"],
            "chunk_id": f"{doc['filename']}_chunk_{i}"
        })

print(f"📄 Total chunks created: {len(all_chunks)}")

# -----------------------------
# Create embeddings
# -----------------------------
texts = [c["text"] for c in all_chunks]
print("🧠 Generating embeddings...")
embeddings = embed_model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

# -----------------------------
# Build FAISS index
# -----------------------------
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# -----------------------------
# Save FAISS index and metadata
# -----------------------------
faiss.write_index(index, INDEX_FILE)
with open(METADATA_FILE, "wb") as f:
    pickle.dump(all_chunks, f)

print(f"✅ FAISS index created with {index.ntotal} vectors")
print(f"💾 Metadata saved to {METADATA_FILE}")
print("🎉 All done. Ready for RAG retrieval!")

