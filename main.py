import streamlit as st
from PIL import Image

file = st.file_uploader('OCRしたい画像をアップロード',type=['png','jpg','jpeg'])

if file:
    img = Image.open(file)
    st.image(
        img,
        caption="アップロードした画像",
        use_container_width = True
        )