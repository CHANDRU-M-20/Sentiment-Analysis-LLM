import os
import azure.cognitiveservices.speech as speechsdk
import streamlit as st
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()
# from sentiment_text import sentiment_analysis



def recognize_from_audio(filename):
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    # st.audio(filename, format="audio/wav") 
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(filename=filename)
       
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)    
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    text = speech_recognition_result.text
    st.subheader("Text Extractions")
    st.write("Audio to Text: {}".format(text))
    return [text]
