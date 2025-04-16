import streamlit as st
import requests

# Load Groq API key securely
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# App UI
st.title("✨ PromptCraft - Your AI Prompt Assistant")

role = st.selectbox("Role", ["teacher", "product marketer", "stand-up comedian", "science explainer"])
tone = st.selectbox("Tone", ["playful", "formal", "inspiring", "sarcastic"])
topic = st.text_input("What should GPT talk about?", "black holes")
audience = st.text_input("Who is the audience?", "middle school students")
length = st.selectbox("How long should the response be?", ["1 sentence", "2-3 sentences", "1 paragraph"])

prompt = f"You are a {role}. Write a {tone} explanation of {topic} for {audience}. Keep it {length}."

# Call Groq API
if st.button("Generate 🎯"):
    with st.spinner("Generating..."):
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mixtral-8x7b-32768",  # or try "llama3-8b-8192"
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            st.markdown("### 💡 Result")
            st.write(result["choices"][0]["message"]["content"])
        else:
            st.error(f"⚠️ Error: {response.status_code} - {response.json()}")
