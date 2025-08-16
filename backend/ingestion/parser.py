import os
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)

        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(full_path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(full_path)
        else:
            continue

        docs.append({
            "filename": filename,
            "text": text
        })
    return docs

# Test run
if __name__ == "__main__":
    folder = "data"
    documents = load_documents(folder)

    for doc in documents:
        print(f"📄 {doc['filename']}")
        print(doc['text'][:500])  # Preview first 500 characters
        print("=" * 60)
