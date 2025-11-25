# Program title: Storytelling App

import streamlit as st
from transformers import pipeline
from PIL import Image

# -------------------------------
# Load Hugging Face pipelines
# -------------------------------
st.title("🖼️ Image-to-Text and Text-to-Speech App")

# Load models
image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
text_to_speech = pipeline("text-to-speech", model="facebook/mms-tts-eng")

# -------------------------------
# Streamlit UI
# -------------------------------
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Step 1: Image-to-Text
    st.write("### Extracting text from image...")
    text_output = image_to_text(image)[0]['generated_text']
    st.write("**Extracted Text:**", text_output)

    # Step 2: Text-to-Speech
    st.write("### Generating speech...")
    speech_output = text_to_speech(text_output)

    # Get the audio array and sample rate
    audio_array = speech_output["audio"]
    sample_rate = speech_output["sampling_rate"]
   
    # Play audio directly using Streamlit
    st.audio(audio_array, sample_rate=sample_rate)
