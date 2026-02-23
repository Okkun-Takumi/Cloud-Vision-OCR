import streamlit as st
from PIL import Image

file_pash = st.file_uploader('',type=['png','jpg','jpeg'])
img = Image.open(file_path)
st.image(img)