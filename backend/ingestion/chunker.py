import nltk
from nltk.tokenize import sent_tokenize

def chunk_text(text, max_tokens=150):
    """
    Splits a long text into chunks of max_tokens (approx),
    preserving sentence boundaries.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    current_tokens = 0

    for sentence in sentences:
        sentence_tokens = len(sentence.split())

        # If adding this sentence would exceed the limit, save current chunk
        if current_tokens + sentence_tokens > max_tokens:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
            current_tokens = sentence_tokens
        else:
            current_chunk += " " + sentence
            current_tokens += sentence_tokens

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def chunk_documents(documents, max_tokens=150):
    """
    Takes a list of parsed documents and returns a list of chunks with metadata.
    """
    all_chunks = []

    for doc in documents:
        cleaned_text = doc['text'].replace("\n", " ").replace("●", "-").replace("​", "")
        chunks = chunk_text(cleaned_text, max_tokens=max_tokens)
        
     
     

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "filename": doc["filename"],
                "chunk_id": f"{doc['filename']}_chunk_{i}",
                "text": chunk
            })

    return all_chunks

# Test it
if __name__ == "__main__":
    from parser import load_documents

    docs = load_documents("data")
    chunks = chunk_documents(docs)

    for c in chunks[:3]:  # Show first 3 chunks
        print(f"📄 {c['filename']} - {c['chunk_id']}")
        print(c["text"][:300])
        print("=" * 60)
