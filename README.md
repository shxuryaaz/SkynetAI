# SkyNetAI

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
SkyNetAI is a versatile and high-performance AI chatbot platform that enables seamless interaction with powerful Large Language Models (LLMs) such as OpenAI GPT, Mistral, Falcon, and Hugging Face-hosted models. It offers a clean, intuitive frontend built with Streamlit and a robust backend powered by FastAPI. Users can tailor the chatbot’s responses to specific domains like finance or technology, making it ideal for both general-purpose and specialized use cases. The application supports secure environment-based API key configuration and is designed to be easily extensible with support for various LLMs and additional modules.

---

## 📦 Tech Stack

| Layer         | Technology                   |
|---------------|-------------------------------|
| Backend       | FastAPI (Python)              |
| Frontend      | Streamlit                     |
| LLM Provider  | HuggingFace / OpenAI          |
| NLP Engine    | Transformers / InferenceClient|
| Env Handling  | `python-dotenv`               |

---

## Getting Started

### 1.Clone the repo

```bash
git clone https://github.com/shxuryaaz/SkynetAI.git
cd SkynetAI
```

### 2.Set up environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 3.Create `.env` file

```env
OPENAI_API_KEY=your_openai_key
HUGGINGFACE_TOKEN=your_huggingface_token
LLM_MODE=openai   # or mistral or falcon
```

### 4.Run the backend API

```bash
uvicorn app.main:app --reload
```

### 5.Launch the UI

```bash
streamlit run streamlit_app/ui.py
```

---

## Screenshot

<p align="center">
  <img src="https://i.ibb.co/tMCVQKYH/initializing.png" width="700" alt="SkynetAI"/>
  <img src="https://i.ibb.co/svfc7VwX/final-screen.png" width="700" alt="SkynetAI2"/>
</p>

---

## 🔧 Configuration

| Variable             | Description                            |
|----------------------|----------------------------------------|
| `OPENAI_API_KEY`     | OpenAI API key                         |
| `HUGGINGFACE_TOKEN`  | Hugging Face token (for gated models)  |
| `LLM_MODE`           | `openai`, `mistral`, or `falcon`       |

---

## Contributing

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

## Contact

Connect with me on [LinkedIn](https://www.linkedin.com/in/shauryasingh28/)
