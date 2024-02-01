import speech_recognition as sr
import streamlit as st

def google_transcriptor():
    stop=False
    r=sr.Recognizer()

    audio_text=open("C:/Users/ass85/PycharmProjects/speech_recognition/.venv/Scripts/Enregistrement.m4a")



    try:
        # using Google Speech Recognition
        text = r.recognize_google(audio_text)
        return text
    except:
        return "Sorry, I did not get that."

print(google_transcriptor())


