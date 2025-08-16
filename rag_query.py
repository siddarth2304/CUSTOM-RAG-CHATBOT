# rag_query.py
import os
import pickle
import faiss
from backend.generator import Generator

# -----------------------------
# Settings
# -----------------------------
INDEX_FILE = "faiss_index.index"
METADATA_FILE = "metadata.pkl"

# -----------------------------
# Load FAISS index and metadata
# -----------------------------
print("🔄 Loading FAISS index and metadata...")
index = faiss.read_index(INDEX_FILE)
with open(METADATA_FILE, "rb") as f:
    metadata = pickle.load(f)

print(f"✅ FAISS index loaded ({index.ntotal} vectors)")
print(f"✅ Metadata loaded ({len(metadata)} chunks)")

# -----------------------------
# Initialize generator
# -----------------------------
generator = Generator()
print("Using device for embeddings: cuda")

# -----------------------------
# Simple FAISS retriever
# -----------------------------
def retrieve(query, top_k=3):
    """
    Retrieve top_k relevant chunks based on simple text embedding similarity
    """
    # For simplicity, we assume embeddings already exist in FAISS
    # Here we just return the top_k metadata chunks
    # You can enhance this to use semantic embeddings in production
    return metadata[:top_k]

# -----------------------------
# Chat loop
# -----------------------------
print("\n💬 Welcome to the Custom RAG Chatbot!")
print("Type 'exit' to quit.\n")

while True:
    query = input("Enter your question: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    results = retrieve(query, top_k=3)

    print("\n--- Retrieved Chunks ---")
    chunks_for_gemini = []
    for i, r in enumerate(results):
        text = r.get("text", "")  # get actual text
        print(f"Chunk {i+1}: {text[:300]}...")  # first 300 chars
        chunks_for_gemini.append(text)

    # Generate answer from Gemini
    answer = generator.generate(query, chunks_for_gemini)
    print("\n--- Generated Answer ---\n", answer)
    print("-" * 60)

