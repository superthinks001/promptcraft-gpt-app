import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("✨ PromptCraft - Your AI Prompt Assistant")

# Inputs
role = st.selectbox("Role", ["teacher", "product marketer", "stand-up comedian", "science explainer"])
tone = st.selectbox("Tone", ["playful", "formal", "inspiring", "sarcastic"])
topic = st.text_input("What should GPT talk about?", "black holes")
audience = st.text_input("Who is the audience?", "middle school students")
length = st.selectbox("How long should the response be?", ["1 sentence", "2-3 sentences", "1 paragraph"])

# (Optional) Model selector
model = st.selectbox("Choose OpenAI model", ["gpt-3.5-turbo", "gpt-4"])

# Prompt builder
prompt = f"You are a {role}. Write a {tone} explanation of {topic} for {audience}. Keep it {length}."

if st.button("Generate 🎯"):
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 Result")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
