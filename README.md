# emotion-detection-app
This is a simple AI-based web application that detects emotions from text.  
It uses **Flask** for web deployment and a **mock Watson NLP fallback** (so it works without an API key).  

---

## 🚀 Features
- Detects emotions like **Joy, Sadness, Anger, Fear, Disgust**  
- Flask-based REST API (`/analyze` endpoint)  
- Handles errors and invalid inputs gracefully  
- Unit tests with **pytest**  
- Code quality checked with **flake8**  
- Mock fallback so **no IBM API key is required**

---

## 📂 Project Structure
emotion-detection-app/
│── app.py # Flask app
│── emotion_app.py # Core logic (Watson API + mock fallback)
│── test_emotion.py # Unit tests
│── requirements.txt # Dependencies
│── README.md # Project documentation
