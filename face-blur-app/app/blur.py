import cv2
import numpy as np

def anonymize_faces(image, blur_strength=45, mode="Blur", whole_image=False, confidence_threshold=0.5):
    if whole_image:
        return apply_blur(image, blur_strength, mode)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    output = image.copy()
    for (x, y, w, h) in faces:
        face_region = output[y:y+h, x:x+w]
        blurred_face = apply_blur(face_region, blur_strength, mode)
        output[y:y+h, x:x+w] = blurred_face

    return output

def apply_blur(region, blur_strength, mode):
    if mode == "Blur":
        k = blur_strength if blur_strength % 2 == 1 else blur_strength + 1
        return cv2.GaussianBlur(region, (k, k), 0)
    elif mode == "Pixelate":
        h, w = region.shape[:2]
        temp = cv2.resize(region, (max(1, w // blur_strength), max(1, h // blur_strength)), interpolation=cv2.INTER_LINEAR)
        return cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
    elif mode == "Black Box":
        return np.zeros_like(region)
    else:
        return region
