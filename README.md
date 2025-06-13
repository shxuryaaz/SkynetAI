# 🤖 Intellichat

> A blazing-fast, intelligent AI chatbot built with **FastAPI**, **Streamlit**, and **LLMs** (like OpenAI / Mistral).

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" />
  <img src="https://img.shields.io/github/license/yourusername/intellichat?style=flat-square" />
  <img src="https://img.shields.io/badge/Powered%20By-LLM-blue?style=flat-square" />
</p>

---

## ✨ Features

- 🔌 Chat with powerful LLMs (OpenAI GPT / Mistral / Falcon / Hugging Face models)
- 🌐 Simple REST API using FastAPI
- 🧠 Choose domain-specific knowledge (e.g., finance, tech)
- 🖥️ Clean web UI using Streamlit
- 🔒 Environment-secured API Key support
- 🦾 Easily extendable with other models and domains

---

## 📦 Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Backend       | FastAPI (Python)         |
| Frontend      | Streamlit                |
| LLM Provider  | HuggingFace / OpenAI     |
| NLP Engine    | Transformers / InferenceClient |
| Env Handling  | `python-dotenv`          |

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/yourusername/intellichat.git
cd intellichat
```

### 2️⃣ Set up environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3️⃣ Create `.env` file

```env
OPENAI_API_KEY=your_openai_key
HUGGINGFACE_TOKEN=your_huggingface_token
LLM_MODE=openai   # or mistral or falcon
```

### 4️⃣ Run the backend API

```bash
uvicorn app.main:app --reload
```

### 5️⃣ Launch the UI

```bash
streamlit run streamlit_app/ui.py
```

---

## 📷 Screenshot

<p align="center">
  <img src="https://your-screenshot-url.com/preview.png" width="700" alt="Intellichat Screenshot"/>
</p>

---

## 🔧 Configuration

| Variable             | Description                            |
|----------------------|----------------------------------------|
| `OPENAI_API_KEY`     | OpenAI API key                         |
| `HUGGINGFACE_TOKEN`  | Hugging Face token (for gated models)  |
| `LLM_MODE`           | `openai`, `mistral`, or `falcon`       |

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

```bash
git checkout -b feature/awesome-feature
git commit -m "Add awesome feature"
git push origin feature/awesome-feature
```

---

## 🛡 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

Made with ❤️ by [@nitrus](https://github.com/yourusername)
