


import streamlit as st
from transformers import pipeline
from PIL import Image

# Streamlit UI
st.title("Age Classification using ViT")

# Load the age classification pipeline
@st.cache_resource
def load_model():
    return pipeline("image-classification", model="nateraw/vit-age-classifier")

age_classifier = load_model()

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Classify age
    with st.spinner("Classifying age..."):
        age_predictions = age_classifier(image)
        age_predictions = sorted(age_predictions, key=lambda x: x['score'], reverse=True)

    # Display results
    st.subheader("Predicted Age Range:")
    st.write(f"**Age range:** {age_predictions[0]['label']}")
    st.write("Full Predictions:")
    for pred in age_predictions:
        st.write(f"{pred['label']}: {pred['score']:.4f}")



