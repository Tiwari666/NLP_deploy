#  NLP Spam Detector – Deployed with Flask + Render

This is a simple yet powerful web app that classifies user messages as **spam** or **ham** using Natural Language Processing (NLP) and Machine Learning.

---

##  Description

This project uses a trained **Scikit-learn model** wrapped in a **Flask** web application and deployed via **Render**. Users can input text and get instant predictions about whether the message is spam.

---

##  Features

-  Spam/Ham message classification  
-  ML model built with Scikit-learn  
-  Flask-based web app  
-  Live online deployment using Render  
-  Clean and simple UI with HTML templates  

---

##  How to Run Locally

###  Step 1: Clone the Repository
```bash
git clone https://github.com/Tiwari666/NLP_deploy.git
cd NLP_deploy/spam_detection/FlaskApp
```

###  Step 2: Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate      # For Linux/macOS
venv\Scripts\activate         # For Windows
```

###  Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

###  Step 4: Run the App
```bash
python app.py
```

Then open your browser and go to:  
**http://127.0.0.1:5000**

⚠️ **Note:** The link `http://127.0.0.1:5000` is for local development purposes only. It will work only on your machine when the Flask app is running. Others will not be able to access your app using this link.


---

##  How to Use Online

The app is deployed live using [Render](https://render.com).

## 🔗 Live Demo
Access the live app here: [Click to try the Spam Detector](https://nlp-spam-detector-deploy.onrender.com)


---

##  Screenshot

 Ham Example: ![image](https://github.com/user-attachments/assets/485d6c4c-2586-411f-80f9-ad9fb9eac4d0)


 Spam Example: ![image](https://github.com/user-attachments/assets/9860f388-69f1-492f-875f-ad2023c256e1)

---

## Project Structure

```
spam_detection/
├── FlaskApp/
│   ├── app.py
│   ├── model/
│   ├── static/
│   ├── templates/
│   └── requirements.txt
├── data/
├── notebook/
└── artifacts/
```

---

Made with ❤️ using Flask, Scikit-learn, and Render.
