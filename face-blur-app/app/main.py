import streamlit as st
import cv2
import numpy as np
from PIL import Image
from blur import anonymize_faces

from utils import load_image, save_image

st.set_page_config(page_title="Face Blur App", layout="centered")
st.title("😎 Face Blur App")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = load_image(uploaded_file)
    image_copy = image.copy()

    # Show original image
    st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Original Image", use_column_width=True)

    # Blur strength slider
    blur_strength = st.slider("Blur Strength", min_value=1, max_value=101, value=45, step=2)

    # Blur mode selection
    blur_mode = st.radio("Blur Mode", ["Entire Image", "Face Only"])

    # Process image
    if st.button("Apply Blur"):
        whole_image = blur_mode == "Entire Image"
        blurred_image = anonymize_faces(image_copy, blur_strength, whole_image=whole_image)

        # Show blurred image
        st.image(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB), caption="Blurred Image", use_column_width=True)

        # Save and provide download
        save_image(blurred_image,"output.jpg")

        from io import BytesIO
        buf = BytesIO()
        Image.fromarray(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)).save(buf, format="JPEG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Blurred Image",
            data=byte_im,
            file_name="blurred_image.jpg",
            mime="image/jpeg"
        )
