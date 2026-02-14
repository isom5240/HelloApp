# Use a pipeline as a high-level helper
from transformers import pipeline
import streamlit as st

pipe = pipeline("text-generation", model="google/gemma-3-270m-it")
messages = [
    {"role": "user", "content": "What can you do?"},
]
answer = pipe(messages)[0]['generated_text'][1]['content']

st.title("ISOM5240")
st.write(answer)



