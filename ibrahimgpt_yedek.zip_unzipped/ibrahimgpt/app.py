from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def query_ollama(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "ibrahimgpt",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

@app.route("/", methods=["GET", "POST"])
def index():
    cevap = ""
    if request.method == "POST":
        prompt = request.form["prompt"]
        cevap = query_ollama(prompt)
    return render_template("index.html", cevap=cevap)

if __name__ == "__main__":
    app.run(debug=True)
