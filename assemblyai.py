import assemblyai as aai

def assebly_model(file_name):
    if file_name==None:
        return "we have a problem"
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(file_name)

        return transcript.text
    except:
        return "i don't understand"
