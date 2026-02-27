
import os
import streamlit as st
from transformers import pipeline
from PIL import Image

st.title("Image-to-Text and Text-to-Speech App")

image_to_text = pipeline(
  "image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
text_to_speech = pipeline(
  "text-to-speech", model="facebook/mms-tts-eng")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
  image = Image.open(uploaded_file)
  st.image(image)
  
  caption = image_to_text(image)[0]["generated_text"]
  st.write("Caption:", caption)
  
  audio = text_to_speech(caption)
  audio_path = "speech.wav"
  with open(audio_path, "wb") as f:
    f.write(audio["audio"])
  
  st.audio(audio_path)
  
