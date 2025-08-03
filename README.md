# face-smile-eye-detection

This project performs real-time face, smile, and eye detection using OpenCV and Haar cascade classifiers. It uses your system's webcam to detect faces, check if a person is smiling, and identify their eyes — all in real time.

🔍 Features
Real-time webcam capture
Face detection using Haar cascades
Eye detection
Smile detection (tuned to reduce false positives)
Live display with detection annotations
Text overlays for status (e.g., "Eyes Detected", "Smiling")

🛠️ Tech Stack
Python
OpenCV (cv2)
Haarcascade classifiers

📦 Installation
Clone the repo:
git clone https://github.com/ShivangGit123/real-time-face-smile-eye-detection.git
cd real-time-face-smile-eye-detection
Install dependencies:
pip install opencv-python

Make sure you have the following Haar cascade files:
haarcascade_frontalface_alt.xml
haarcascade_eye.xml
haarcascade_smile.xml

You can download them from the OpenCV GitHub Repo and place them in the project folder.

🚀 How to Run
python face_smile_eye_detector.py
Press q to quit the webcam window.

🧠 Detection Tuning
Eye detection parameters: scaleFactor=1.01, minNeighbors=5
Smile detection parameters: scaleFactor=1.5, minNeighbors=20
(Tuned for better accuracy and reduced over-detection)

📄 License
This project is open source and available under the MIT License.
