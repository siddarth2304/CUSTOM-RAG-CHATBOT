# backend/generator.py
import os
from google import genai  # Gemini SDK

class Generator:
    def __init__(self, model="gemini-2.5-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set in environment")
        self.client = genai.Client(api_key=self.api_key)
        self.model = model

    def generate(self, query, chunks):
        """
        query: str
        chunks: list of strings (retrieved chunk texts)
        """
        # Combine all chunks as context
        context = "\n".join(chunks)
        prompt = f"Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

        # ✅ Gemini SDK call for latest version
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text

