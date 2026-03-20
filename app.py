import streamlit as st
import os
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
genai.configure(api_key=os.getenv("Gemini API Key"))

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}
safety_settings = {
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

model = genai.GenerativeModel(
    model_name='gemini-2.0-flash',
    safety_settings=safety_settings
)
st.title("AI Blog Application")
st.subheader("Welcome to the AI-powered blogging platform!")
blog="This is a sample blog post generated using AI. You can create your own posts and share them with the world!"
with st.sidebar:
    st.title("Input your blog topic")
    st.subheader("Enter a topic for your blog post:")

    blog_topic = st.text_input("Blog Topic", "AI in Blogging")

    keywords = st.text_input("Keywords (comma separated)", "AI, Blogging, Technology")  
    num_words = st.slider("Number of Words", min_value=100, max_value=1000, value=500, step=50) 
    if st.button("Generate Blog Post"):
        prompt = f"Write a blog post about {blog_topic} using the following keywords: {keywords}. The blog post should be approximately {num_words} words long."
        response = model.generate_content(prompt)
        blog = response.text
submit_button = st.button("Submit Blog Post")
if submit_button:
    st.success("Blog post submitted successfully!")
    st.write(blog)


