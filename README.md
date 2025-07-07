# langchain-search-chatbot
# 🔎 LangChain Search Chatbot

A conversational agent built with [LangChain](https://www.langchain.com/), [Groq LLMs](https://console.groq.com/), and [Streamlit](https://streamlit.io/) that can search the web using:
- 🔍 DuckDuckGo
- 📚 Wikipedia
- 📄 ArXiv academic papers

The chatbot thinks step-by-step and shows its reasoning using LangChain's StreamlitCallbackHandler.

## 🖼️ Demo UI

![Demo Screenshot](https://user-images.githubusercontent.com/your-image.png) <!-- optional placeholder -->

---

## 🚀 Features

- ✅ Real-time web search using DuckDuckGo
- ✅ Contextual academic search from Arxiv
- ✅ Quick summaries from Wikipedia
- ✅ Multi-tool LangChain Agent
- ✅ Visual trace of reasoning steps in Streamlit

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langchain-search-chatbot.git
cd langchain-search-chatbot
````

### 2. Create and activate virtual environment (optional but recommended)

```bash
python -m venv generativeai
# Windows
.\generativeai\Scripts\activate
# macOS/Linux
source generativeai/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` doesn't exist yet, you can generate it with:

```bash
pip freeze > requirements.txt
```

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🔑 API Key Setup

You'll need a [Groq API key](https://console.groq.com/) to run the chatbot. Enter it in the sidebar when the app starts.

---

## 📦 Dependencies

* `streamlit`
* `langchain`
* `langchain_community`
* `langchain_groq`
* `python-dotenv` *(if you want to use a `.env` file)*

---

## 📁 File Structure

```text
.
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## ✨ Example Questions

Try asking:

* "What is reinforcement learning?"
* "Who won the Nobel Prize in Physics 2022?"
* "Summarize a recent paper about large language models from Arxiv"

---

## 🧠 Built With

* [LangChain](https://www.langchain.com/)
* [Groq](https://console.groq.com/)
* [Streamlit](https://streamlit.io/)
* [DuckDuckGo Search](https://duckduckgo.com/)
* [Arxiv](https://arxiv.org/)
* [Wikipedia](https://www.wikipedia.org/)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 📬 Contact

For help or collaboration, feel free to reach out via [GitHub Issues](https://github.com/your-username/langchain-search-chatbot/issues).

```

