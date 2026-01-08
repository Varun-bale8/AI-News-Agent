from flask import Flask, request, render_template
from newspaper import Article
from transformers import pipeline
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    summary_hindi = ""
    if request.method == "POST":
        url = request.form["url"]
        
        # Extract
        article = Article(url)
        article.download()
        article.parse()
        full_text = article.text
        
        # Summarize
        summary = summarizer(full_text, max_length=120, min_length=30, do_sample=False)[0]['summary_text']
        
        # Translate
        translated = translator.translate(summary, src='en', dest='hi').text
        summary_hindi = translated
        
        # Convert to Speech
        tts = gTTS(text=translated, lang='hi')
        tts.save("static/summary.mp3")
    
    return render_template("index.html", summary=summary_hindi)

if __name__ == "__main__":
    app.run(debug=True)
