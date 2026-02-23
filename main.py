import streamlit as st
from PIL import Image
from google.cloud import vision
from google.oauth2 import service_account
import requests

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

    # base64変換
    content = base64.b64encode(
        file.getvalue()
    ).decode("utf-8")

    url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"

    request_body = {
        "requests":[
            {
                "image":{
                    "content":content
                },
                "features":[
                    {
                        "type":"TEXT_DETECTION"
                    }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        json=request_body
    )

    result = response.json()
    st.write(result)


    # try:

    #     text = result["responses"][0]["textAnnotations"][0]["description"]

    #     st.subheader("OCR Result")

    #     st.write(text)

    # except:
    #     st.write("文字が検出されませんでした")