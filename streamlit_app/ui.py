import streamlit as st
import time
import requests

# Page setup
st.set_page_config(page_title="SkynetAI", layout="centered")

# CSS Styles
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');

body, .stApp {
    background-color: black;
    font-family: 'Share Tech Mono', monospace;
    color: #ff4c4c;
}

img.skynet-logo {
    display: block;
    margin: 0 auto;
    width: 300px;
    margin-top: 2rem;
    filter: blur(2px);
    opacity: 0.6;
}

@keyframes glitch {
  0% { text-shadow: 2px 2px red; }
  20% { text-shadow: -2px -2px #ff0000; }
  40% { text-shadow: 2px -2px #ff4c4c; }
  60% { text-shadow: -2px 2px #ff0000; }
  80% { text-shadow: 2px 2px red; }
  100% { text-shadow: 0 0 10px red; }
}

.glitch-text {
    font-size: 2.5rem;
    font-weight: bold;
    text-align: center;
    animation: glitch 1s infinite;
    margin-top: 5vh;
    color: #ff1a1a;
    text-shadow: 0 0 15px red;
}

.subtitle {
    font-size: 1.2rem;
    color: #ff4c4c;
    text-align: center;
    margin-bottom: 2rem;
    font-style: italic;
    text-shadow: 0 0 6px #ff1a1a;
}

.stTextInput>div>div>input {
    background-color: #0e0e0e;
    border: 2px solid #ff4c4c;
    border-radius: 10px;
    font-size: 1.2rem;
    color: #ffcccc;
    padding: 12px;
    box-shadow: 0 0 12px #ff1a1a;
}
.stTextInput>div>div>input:focus {
    border-color: #ff0000;
    box-shadow: 0 0 18px red;
}

.stSelectbox > div {
    background-color: #0e0e0e;
    border: 2px solid #ff4c4c !important;
    border-radius: 10px;
}
.stSelectbox > div > div {
    font-size: 1.1rem;
    color: #ffcccc;
    padding: 10px;
}

div.stButton > button {
    background-color: #ff1a1a;
    color: black;
    font-size: 1.2rem;
    font-weight: bold;
    padding: 10px 30px;
    border-radius: 12px;
    border: none;
    box-shadow: 0 0 12px red;
    cursor: pointer;
}
div.stButton > button:hover {
    background-color: #ff0000;
    box-shadow: 0 0 20px red;
}

.response {
    background-color: #111;
    border: 2px solid #ff4c4c;
    border-radius: 10px;
    padding: 20px;
    color: #ffdddd;
    font-size: 1.1rem;
    margin-top: 2rem;
    white-space: pre-wrap;
}

.typewriter {
  overflow: hidden;
  border-right: .15em solid red;
  white-space: nowrap;
  animation:
    typing 2.5s steps(40, end),
    blink-caret .75s step-end infinite;
  font-size: 1.1rem;
}

@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}
@keyframes blink-caret {
  from, to { border-color: transparent }
  50% { border-color: red; }
}
</style>
""", unsafe_allow_html=True)

# Show background image (blurred logo)
st.markdown("""
<img src="https://i.ibb.co/rG3wXqPG/skynet-logo.png" alt="skynet-logo" class="skynet-logo"/>
""", unsafe_allow_html=True)

# SPLASH SCREEN using container
if "boot_complete" not in st.session_state:
    st.session_state.boot_complete = False

if not st.session_state.boot_complete:
    splash = st.empty()
    with splash.container():
        st.markdown('<div class="glitch-text">Initializing SkynetAI...</div>', unsafe_allow_html=True)
    time.sleep(2.5)
    splash.empty()
    st.session_state.boot_complete = True

# MAIN UI
st.markdown('<h1 class="subtitle">Welcome to SkynetAI - Terminal Interface</h1>', unsafe_allow_html=True)

col1, col2 = st.columns([2.5, 1.5])
with col1:
    query = st.text_input("Enter your question:")
with col2:
    domain = st.selectbox("Select Domain", ["general", "finance", "medical", "legal"])

if st.button("Ask SkynetAI"):
    if not query.strip():
        st.warning("Please type a question.")
    else:
        with st.spinner("Skynet is processing..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/chat/",
                    json={"query": query, "domain": domain}
                )
                if response.status_code == 200:
                    answer = response.json().get("response", "No response received.")
                    st.markdown(f'<div class="response"><div class="typewriter">{answer}</div></div>', unsafe_allow_html=True)
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
