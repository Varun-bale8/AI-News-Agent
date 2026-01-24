from flask import Flask, request, render_template
from newspaper import Article
from transformers import pipeline
from gtts import gTTS
import os

app = Flask(__name__)

# Load summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/", methods=["GET", "POST"])
def index():
    summary_english = ""
    
    if request.method == "POST":
        url = request.form["url"]
        
        # Extract article
        article = Article(url)
        article.download()
        article.parse()
        full_text = article.text
        
        # Summarize (English)
        summary = summarizer(
            full_text,
            max_length=120,
            min_length=30,
            do_sample=False
        )[0]['summary_text']
        
        summary_english = summary
        
        # Convert English summary to speech
        tts = gTTS(text=summary, lang='en')
        tts.save("static/summary.mp3")
    
    return render_template("index.html", summary=summary_english)

if __name__ == "__main__":
    app.run(debug=True)
