import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            freya_voice(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            freya_voice("Sorry, I did not get that")
        except sr.RequestError:
            freya_voice("Sorry, my speech service is down right now")
        return voice_data

def freya_voice(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def freya_respond(voice_data):
    if 'what is your name' in voice_data:
        freya_voice('You can call me Freya')
    if 'what time is it' in voice_data:
        freya_voice(ctime())
    if 'search' in voice_data:
        search = record_audio('What are we searching for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        freya_voice('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('Which location are we looking up?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        freya_voice('Here is the location of ' + location)
    if 'go to sleep' in voice_data:
        freya_voice('Goodbye')
        exit()

time.sleep(1)
freya_voice("How can I help you?")
while 1:
    voice_data = record_audio()
    freya_respond(voice_data)
