import streamlit as st
import requests

# Load Groq API key securely from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

st.title("✨ PromptCraft - Your AI Prompt Assistant (Groq Edition)")

# User Inputs
role = st.selectbox("Role", ["teacher", "product marketer", "stand-up comedian", "science explainer"])
tone = st.selectbox("Tone", ["playful", "formal", "inspiring", "sarcastic"])
topic = st.text_input("What should the model talk about?", "black holes")
audience = st.text_input("Who is the audience?", "middle school students")
length = st.selectbox("How long should the response be?", ["1 sentence", "2-3 sentences", "1 paragraph"])

# Build prompt
prompt = f"You are a {role}. Write a {tone} explanation of {topic} for {audience}. Keep it {length}."

# Groq endpoint setup
endpoint = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "model": "mixtral-8x7b-32768",  # You can switch to "llama2-70b-4096" or "gemma-7b-it"
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7
}

if st.button("Generate 🎯"):
    with st.spinner("Groq is thinking..."):
        try:
            response = requests.post(endpoint, headers=headers, json=payload)
            result = response.json()
            output = result["choices"][0]["message"]["content"]
            st.markdown("### 💡 Result")
            st.write(output)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
