
import streamlit as st
from transformers import pipeline
from PIL import Image
import numpy as np
from io import BytesIO
from scipy.io.wavfile import write as wav_write  # comes with SciPy

st.title("Image-to-Text and Text-to-Speech App")

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
text_to_speech = pipeline("text-to-speech", model="facebook/mms-tts-eng")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    caption = image_to_text(image)[0]["generated_text"]
    st.write("Caption:", caption)

    tts_out = text_to_speech(caption)

    # Normalize output structure
    if isinstance(tts_out.get("audio"), dict):
        samples = tts_out["audio"]["array"]
        sr = tts_out["audio"]["sampling_rate"]
    else:
        samples = tts_out["audio"]
        sr = tts_out["sampling_rate"]

    # Ensure float32 in [-1, 1]
    samples = np.asarray(samples)
    if samples.dtype != np.float32:
        samples = samples.astype(np.float32)
    max_abs = np.max(np.abs(samples)) if samples.size else 1.0
    if max_abs > 1.0:
        samples = samples / max_abs

    # Encode to WAV in memory
    wav_buf = BytesIO()
    wav_write(wav_buf, sr, samples)  # scipy.io.wavfile.write
    wav_buf.seek(0)

    # Play
    st.audio(wav_buf, format="audio/wav")

  
