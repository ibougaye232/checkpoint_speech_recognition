import speech_recognition as sr

def google_transcriptor(file_name,lang):
    r = sr.Recognizer()

    try:
        with sr.AudioFile(file_name) as source:
            audio_text = r.record(source)
            text = r.recognize_google(audio_text,language=lang)
            return text
    except:
        return "Sorry, I did not get that."


