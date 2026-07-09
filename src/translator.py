import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:4b"


def translate_to_english(text):

    if not text.strip():
        return ""

    prompt = f"""
Translate the following text into natural English.

Rules:
- Translate only.
- Do not explain.
- Do not add comments.
- If the text is already English, return it unchanged.

Text:

{text}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=1800
    )

    return response.json()["response"].strip()