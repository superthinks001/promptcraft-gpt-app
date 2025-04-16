import streamlit as st
import requests

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

st.title("✨ PromptCraft - Your AI Prompt Assistant (Groq Edition)")

role = st.selectbox("Role", ["teacher", "product marketer", "stand-up comedian", "science explainer"])
tone = st.selectbox("Tone", ["playful", "formal", "inspiring", "sarcastic"])
topic = st.text_input("What should the assistant talk about?", "black holes")
audience = st.text_input("Who is the audience?", "middle school students")
length = st.selectbox("How long should the response be?", ["1 sentence", "2-3 sentences", "1 paragraph"])

prompt = f"You are a {role}. Write a {tone} explanation of {topic} for {audience}. Keep it {length}."

if st.button("Generate 🎯"):
    with st.spinner("Groq is thinking..."):
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }

        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        response = res.json()
        st.markdown("### 💡 Result")
        st.write(response["choices"][0]["message"]["content"])
