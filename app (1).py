import streamlit as st
import requests
import base64

# === YOUR OPENROUTER KEY ===
api_key = "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"  # Replace with your actual key

# === PAGE CONFIG ===
st.set_page_config(
    page_title="✨ PromptCrafter by Sandhiya",
    page_icon="🪄",
    layout="centered"
)

# === CUSTOM CSS ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #fdf6f0, #f0f8ff);
        color: #000000;
    }
    h1, h2, h3 {
        color: #6A0DAD;
    }
    .stButton>button {
        background-color: #6A0DAD;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #9A32CD;
        color: #ffffff;
    }
    .prompt-box {
        background-color: #fff8e7;
        padding: 20px;
        border-left: 5px solid #ff69b4;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 2px 2px 8px #ddd;
    }
    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# === OPTIONAL LOGO ===
st.image("https://i.imgur.com/kHkk9Mn.png", use_container_width=True)

# === TITLE ===
st.title("✨ PromptCrafter")
st.markdown("Unleash your imagination with AI-powered prompt generation 💫")

# === INPUTS ===
use_case = st.selectbox("🧠 Use Case", 
    ["Creative Writing", "Coding Help", "Study Aid", "Social Media", "Job Interview", "Midjourney Prompt"])
tone = st.selectbox("🎭 Tone", 
    ["Neutral", "Friendly", "Professional", "Funny", "Motivational"])
details = st.text_area("✍️ Describe what your prompt should help with")

# === FUNCTION ===
def generate_prompt(use_case, tone, details):
    full_prompt = f"Create a powerful prompt for:\nUse Case: {use_case}\nTone: {tone}\nDetails: {details}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openrouter/mistral-7b",
        "messages": [{"role": "user", "content": full_prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        st.error("🚨 Oops! Something went wrong while generating the prompt.")
        st.code(response.text)
        return None

# === GENERATE BUTTON ===
if st.button("🎯 Generate Prompt"):
    if details:
        result = generate_prompt(use_case, tone, details)
        if result:
            st.markdown("#### 🪄 Generated Prompt:")
            st.markdown(f'<div class="prompt-box">{result}</div>', unsafe_allow_html=True)

            b64 = base64.b64encode(result.encode()).decode()
            st.markdown(f'<a href="data:file/txt;base64,{b64}" download="prompt.txt">📥 Download this Prompt</a>', unsafe_allow_html=True)
    else:
        st.warning("Please describe your prompt first!")

# === FOOTER ===
st.markdown("""<hr style='margin-top:30px;'>
<div style='text-align:center;'>
    🧠 Made with ❤️ by <b>Sandhiya</b> | AI & DS Final Year Student ✨<br>
    <a href="https://github.com/yourusername" target="_blank">GitHub</a> | 
    <a href="mailto:youremail@example.com">Email Me</a>
</div>
""", unsafe_allow_html=True)

