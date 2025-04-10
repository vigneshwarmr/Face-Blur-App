# utils.py
import cv2
import numpy as np

def load_image(uploaded_file):
    try:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        return image
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, filename):
    cv2.imwrite(filename, image)
