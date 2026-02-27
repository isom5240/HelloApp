


import streamlit as st
from transformers import pipeline

# Use st.cache_resource to load the model once across all user sessions
@st.cache_resource
def get_model():
    # Load a pre-trained sentiment-analysis model from the Hugging Face Model Hub
    # You can find other models at https://huggingface.co/models
    model = pipeline("sentiment-analysis")
    return model

st.title("Hugging Face Sentiment Analysis Demo")

st.markdown("Enter text below to classify its sentiment (positive or negative).")

# Get the model
sentiment_pipeline = get_model()

# Create an input text box for the user
input_text = st.text_input("Enter your text here:", "I love building AI apps with Streamlit!")

# Create a button to trigger the analysis
if st.button("Analyze Sentiment"):
    if input_text:
        # Perform inference using the loaded model
        result = sentiment_pipeline(input_text)
        label = result[0]['label']
        score = result[0]['score']

        st.write("---")
        st.write(f"**Prediction:** {label}")
        st.write(f"**Confidence Score:** {score:.2f}")
        st.write("---")
    else:
        st.warning("Please enter some text for analysis.")
