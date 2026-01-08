# 📰 AI News Agent (Hindi News Summarizer)

An **AI-powered News Agent** that extracts news articles from a given URL, **summarizes the content using NLP**, **translates the summary into Hindi**, and **converts it into speech**. This project demonstrates practical usage of **Flask**, **Transformers**, and **Generative AI** for real-world applications.

---

## 🚀 Project Overview

The AI News Agent allows users to:

1. Enter a **news article URL**
2. Automatically **extract the article content**
3. **Summarize** the article using a pre-trained NLP model
4. **Translate** the summary from English to Hindi
5. **Convert** the Hindi summary into **audio (Text-to-Speech)**

This project is ideal for beginners exploring **AI + Web Development + NLP**.

---

## ✨ Features

*  Article extraction from online news links
*  AI-based text summarization
*  English → Hindi translation
*  Hindi Text-to-Speech output
*  Simple and user-friendly web interface

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **NLP Model:** Facebook BART (via Hugging Face Transformers)
* **Article Extraction:** Newspaper3k
* **Translation:** GoogleTrans
* **Text-to-Speech:** gTTS
* **Frontend:** HTML, CSS (Flask Templates)

---

## 📁 Project Structure

```
AI-News-Agent/
│── app.py
│── templates/
│   └── index.html
│── static/
│   └── summary.mp3
│── testlink.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-news-agent.git
cd ai-news-agent
```

### 2️⃣ Install Required Libraries

```bash
pip install flask newspaper3k transformers googletrans==4.0.0-rc1 gtts torch
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

##  How It Works

1. User submits a **news article URL**
2. Article text is extracted using **Newspaper3k**
3. Text is summarized using **BART Transformer model**
4. Summary is translated into **Hindi**
5. Hindi text is converted into **speech (MP3)**

---

## 📌 Use Cases

* News summarization for regional language users
* AI-powered content consumption
* NLP and GenAI learning project
* Resume / Portfolio project

---

##  Future Improvements

* Support for multiple Indian languages
* Voice input for URLs
* Improved UI/UX
* Deployment on cloud (AWS / Azure / Render)
* Mobile-friendly interface

---

##  Author

**Bale Varun**
AI/ML Enthusiast | Data Science & NLP Learner

---

## ⭐ Acknowledgements

* Hugging Face Transformers
* Flask Community
* Open-source NLP ecosystem

---

⭐ If you like this project, don’t forget to **star the repository** on GitHub!
