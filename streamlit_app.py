import streamlit as st
import openai

openai.api_key = st.sidebar.text_input("Enter your OpenAI API Key:", value="", type="password")

st.header("DALL-E 2 prompting")

with st.form("prompt_form"):
    prompt = st.text_input("Enter your prompt:", value="")
    n_generations = st.number_input("Enter the number of generations:", value=1, min_value=1, max_value=4, step=1)
    size = st.selectbox("Select the size of the image:", options=["1024x1024", "512x512", "256x256"])

    submitted = st.form_submit_button("Submit")
    if submitted:
        response = openai.Image.create(
            prompt = prompt,
            n = n_generations,
            size = size
        )

        for i in range(n_generations):
            st.image(response['data'][i]['url'])