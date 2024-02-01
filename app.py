#importation des bibliothéques
import streamlit as st
import pandas as pd
from google_model_test import google_transcriptor
from recorder import recorder2
import speech_recognition as sr
from assemblyai import assebly_model


def save_text(text):
    with open("le_texte.txt","w") as fichier:
        fichier.write(text)

def main():
    st.title("Welcome to the ibrahima's speech recognizer, use you")

    #choix du model de reconnaissance d'image
    choice=st.selectbox("choose your speech_recognition model:",["google","assemblyai"])



    #choix de la langue
    lang=st.selectbox("choose your language:",["en-GB","fr-FR","es-ES"])

    audio=None

    #transcription
    if st.button("click to record"):
        audio=recorder2()

    #déclenchement du modéle

    st.write(audio)

    text=google_transcriptor(audio,lang)

    #le texte transcrit
    st.write("the transcription:", text)
    #choix d'enregistrer le texte
    if st.button("do you want to save the text?"):
        save_text(text)

main()




