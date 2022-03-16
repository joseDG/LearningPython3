from google.cloud import texttospeech
from google.cloud import texttospeech_v1
import pdfplumber

import os


text= ""
with pdfplumber.open(r'C:\Users\Mike\Desktop\wp.pdf') as pdf:
    for page in pdf.pages:
      
        text += page.extract_text()
    #print(first_page.extract_text())




os.environ['GOOGLE_APPLICATION_CREDENTIALS']="C:/Users/Mike/Downloads/nimble-yen-344011-522a713efd44.json"

client = texttospeech_v1.TextToSpeechClient()
synthesis_input = texttospeech_v1.SynthesisInput(text=text)
voice = texttospeech_v1.VoiceSelectionParams(
  language_code = 'en-us', ssml_gender = texttospeech_v1.SsmlVoiceGender.FEMALE)

audio_config = texttospeech.AudioConfig(
  audio_encoding= texttospeech_v1.AudioEncoding.MP3
)

response = client.synthesize_speech(
  input=synthesis_input, voice=voice, audio_config=audio_config
)

with open('audiobook.mp3', 'wb') as out:
  out.write(response.audio_content)