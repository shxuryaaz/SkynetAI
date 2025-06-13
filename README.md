# 🤖 SkyNetAI

> A blazing-fast, intelligent AI chatbot built with **FastAPI**, **Streamlit**, and **LLMs** (like OpenAI / Mistral / Falcon).

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" />
  <img src="https://img.shields.io/badge/Powered%20By-LLM-blue?style=flat-square" />
</p>

<p align="center">
  <img src="skynet_logo.png" alt="SkyNet Logo" width="120"/>
</p>

---

## Features

SkyNetAI is a powerful, modular AI chatbot framework built for intelligent and scalable interaction with advanced language models. It combines a responsive web interface using **Streamlit** with a high-performance backend powered by **FastAPI**. SkyNetAI supports major LLMs like **OpenAI**, **Mistral**, **Falcon**, and models hosted on **Hugging Face**, enabling users to deploy domain-specific bots tailored to sectors like finance, education, or tech. It features secure `.env`-based API key management and an architecture that makes adding new models or features simple and intuitive.

---

## How It Works – NLP & LLM Integration

SkyNetAI utilizes advanced **Natural Language Processing (NLP)** capabilities through state-of-the-art **Large Language Models (LLMs)**. Using APIs like OpenAI or Hugging Face's InferenceClient, user inputs are processed using **transformer architectures** such as GPT, Mistral, or Falcon.

These LLMs are capable of:
- Understanding natural human language with context
- Extracting relevant information from input queries
- Generating meaningful, fluent, and context-aware replies
- Adapting behavior based on selected domains like finance, tech, or general-purpose

SkyNetAI abstracts the complexity of NLP via tools like Hugging Face Transformers and exposes a clean FastAPI interface to integrate easily with frontend or other services. This makes it a great foundation for chatbot apps, knowledge assistants, and custom LLM-based tools.

---

## Tech Stack

| Layer         | Technology                   |
|---------------|-------------------------------|
| Backend       | FastAPI (Python)              |
| Frontend      | Streamlit                     |
| LLM Provider  | HuggingFace / OpenAI          |
| NLP Engine    | Transformers / InferenceClient|
| Env Handling  | `python-dotenv`               |

---

##  Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/shxuryaaz/SkynetAI.git
cd SkynetAI
```

### 2. Set up environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3. Create `.env` file

```env
OPENAI_API_KEY=your_openai_key
HUGGINGFACE_TOKEN=your_huggingface_token
LLM_MODE=openai   # or mistral or falcon
```

### 4. Run the backend API

```bash
uvicorn app.main:app --reload
```

### 5. Launch the UI

```bash
streamlit run streamlit_app/ui.py
```

---

## 📸 Screenshot

<p align="center">
  <img src="https://i.ibb.co/tMCVQKYH/initializing.png" width="700" alt="SkynetAI"/>
  <img src="https://i.ibb.co/svfc7VwX/final-screen.png" width="700" alt="SkynetAI2"/>
</p>

---

##  Configuration

| Variable             | Description                            |
|----------------------|----------------------------------------|
| `OPENAI_API_KEY`     | OpenAI API key                         |
| `HUGGINGFACE_TOKEN`  | Hugging Face token (for gated models)  |
| `LLM_MODE`           | `openai`, `mistral`, or `falcon`       |

---

##  Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

```bash
git checkout -b feature/awesome-feature
git commit -m "Add awesome feature"
git push origin feature/awesome-feature
```

---

## 🛡 License

This project is licensed under the MIT License  
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📬 Contact

Connect with me on [LinkedIn](https://www.linkedin.com/in/shauryasingh28/)
