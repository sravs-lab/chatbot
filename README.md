# Chatbot Pages

This folder contains different Streamlit app pages for various chatbot functionalities:

## 1. Text Chatbot (`1_chatbot_text.py`)
A simple chatbot interface for text-based queries using Google's Gemini model.

## 2. Image Chatbot (`2_chatbot_image.py`)
Allows users to upload an image and ask questions about it. The chatbot responds based on both the image and the user's query.

## 3. Audio Chatbot (`3_chatbot_audio.py`)
Enables users to upload an audio file and ask questions related to its content. The chatbot processes the audio and provides relevant responses.

## 4. Translate Chatbot (`4_chatbot_translate.py`)
Provides a text area for users to input text and receive a translated version using the Gemini model.

---

Each page uses Streamlit for the UI and Google Generative AI (Gemini) for generating responses.  
Make sure to set your `GOOGLE_API_KEY` in the environment for the apps to work.
