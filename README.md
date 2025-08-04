#ai_agent
**University Help Desk**
**Overview**
This project is a University Help Desk web app built with Django. It lets users ask questions by voice or text and get replies both as spoken audio and text. The interface uses HTML, CSS, and JavaScript for a smooth and modern user experience. It’s designed to help students and visitors find university info quickly and easily.

**Features**
Voice input (speech-to-text)

Voice and text replies (text-to-speech)

Simple chat-like interface

Clean, user-friendly UI built with HTML/CSS/JS

Powered by Django backend

**Tech Stack**
Backend: Django (Python)

Frontend: HTML5, CSS3, JavaScript

Voice input/output: SpeechRecognition, pyttsx3, or browser Web Speech API

Django templates for rendering pages
**Setup Instructions****
Clone the repo:**
git clone https://github.com/bismil123-crypto/ai_agent.git
cd ai_agent
Create and activate a **virtual environment**:
python -m venv venv
# Windows:
venv\Scripts\activate

**Install dependencies:**
pip install -r requirements.txt

Apply **database migrations**:
python manage.py migrate

**Run the server:**
python manage.py runserver

Open your **browser** at http://127.0.0.1:8000 to use the app.
