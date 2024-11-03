from flask import Flask, request, render_template, jsonify
from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import spacy

app = Flask(__name__)

# Load spaCy model and Hugging Face model
nlp = spacy.load("en_core_web_sm")
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", revision="564e9b5")

# Scrape website content
def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text
    else:
        return None

# Preprocess text for the QA model
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint for answering questions
@app.route("/ask", methods=["POST"])
def ask_question():
    url = request.form.get("url")
    question = request.form.get("question")
    
    # Scrape and preprocess text
    raw_text = scrape_website(url)
    if raw_text:
        cleaned_text = preprocess_text(raw_text)
        answer = qa_pipeline(question=question, context=cleaned_text)['answer']
        return jsonify({"answer": answer})
    else:
        return jsonify({"error": "Failed to retrieve content from the website."})

if __name__ == "__main__":
    app.run(debug=True)
