import streamlit as st
from PIL import Image
from google.cloud import vision
from google.oauth2 import service_account

import base64

file = st.file_uploader('OCRしたい画像をアップロード',type=['png','jpg','jpeg'])

if file:
    img = Image.open(file)
    st.image(
        img,
        caption="アップロードした画像",
        use_container_width = True
        )

    #OCR
    # API KEY
    api_key = st.secrets["VISION_API_KEY"]

    # Vision API client
    client = vision.ImageAnnotatorClient(
        client_options={
            "api_key": api_key
        }
    )

    # バイトデータ取得
    content = file.read()

    image = vision.Image(
        content=content
    )

    # OCR実行
    response = client.text_detection(
        image=image
    )

    texts = response.text_annotations

    # 結果表示
    if texts:

        st.subheader("OCR Result")

        st.write(texts[0].description)

    else:
        st.write("文字が検出されませんでした")