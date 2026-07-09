import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "qwen3:8b",
    "prompt": "Translate this Gujarati sentence into English: તમારું નામ શું છે?",
    "stream": False
}

response = requests.post(url, json=payload)

print("=" * 50)
print(response.json()["response"])
print("=" * 50)