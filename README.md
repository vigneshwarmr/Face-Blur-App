
---

```markdown
# 🕵️‍♀️ Face Blur App

A lightweight web application built with Streamlit and OpenCV that detects and blurs faces in images or videos for privacy protection. Ideal for journalists, researchers,
and anyone who wants to anonymize faces quickly and easily.

---

## ✨ Features

- ✅ Detects faces using OpenCV's Haar Cascade or custom models
- 🌀 Automatically applies a blur effect to detected faces
- 📁 Supports image and video file uploads
- 🔁 Displays both original and blurred versions
- 🌐 Built using Streamlit for an intuitive browser-based UI

---

## 📦 Installation

```bash
git clone https://github.com/vigneshwarmr/Face-Blur-App.git
cd Face-Blur-App
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

##  Run the App

```bash
streamlit run app.py
```

(`http://localhost:8501`).

---

## 🗂️ Project Structure

```
Face-Blur-App/
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── helpers/                # Utility functions (e.g., face detection)
│   └── face_utils.py
├── samples/                # Test images/videos
├── .gitignore
└── README.md
```

---

## ⚙️ Dependencies

- Python 3.8+
- OpenCV
- Streamlit
- NumPy

To install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🙋‍♂️ Author

**M.R.Vigneshwar**
[GitHub](https://github.com/vigneshwarmr)
