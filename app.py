import time
import requests
from flask import Flask, jsonify

app = Flask(__name__)

SITES = [
    "https://httpbin.org/get",
    "https://example.com",
    "https://jsonplaceholder.typicode.com/posts/1"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Referer": "https://www.google.com/"
}

@app.route('/')
def index():
    results = []
    for url in SITES:
        try:
            print(f"🌍 Visitando {url} ...")
            r = requests.get(url, headers=HEADERS, timeout=10)
            results.append({
                "url": url,
                "status": r.status_code,
                "preview": r.text[:100]
            })
        except Exception as e:
            results.append({"url": url, "error": str(e)})
    return jsonify(results)

if __name__ == "__main__":
    print("🚀 Avvio AntAutosurf su Render...")
    app.run(host="0.0.0.0", port=10000)
