import requests 
from flask import Flask, render_template, request

app = Flask(__name__)

df summarize_text(text):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": text}
        ],
        "temperature" : 0.5
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Summarization failed."

if __name__ == "__main__":
    app.run(debug = True)
    