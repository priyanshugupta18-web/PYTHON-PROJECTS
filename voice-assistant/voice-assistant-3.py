import webbrowser as wb             #for web navigation
import subprocess as sb             #for app navigation
import speech_recognition as sr         #for speech to text conversion
import urllib.parse         #for converting normal text to encoded query
from gtts import gTTS           #text to speech(audio file(.mp3)) conversion
from playsound import playsound         #for converting the speech into voice
import os
import uuid

#function for text to speech converrsion
def speak(text):
    filename = f"{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="en", tld = "com.au", slow = False)
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")

#function for speech to text conversion
r = sr.Recognizer()
def listen():
        with sr.Microphone() as source:
            return r.listen(source)

print("HEY THERE!")
speak("Hey there")
speak("Enter the input medium")
inp_med = input("ENTER THE INPUT MEDIUM(VOICE/TEXT): ")

if (inp_med.lower() == "voice"):            #operations in case of voice input
    print("YOU HAVE CHOOSEN VOICE INPUT AS A MEDIUM")
    speak("You have choosen voice input as a medium")
    print("PLEASE SPEAK NOW...")
    speak("Please speak now!")

    audio = listen()

    print("YOU SAID,", r.recognize_google(audio).upper())
    speak(f"You said, {r.recognize_google(audio).upper()}")

    command = r.recognize_google(audio).lower()

    encoded_query = urllib.parse.quote(command)         #parsing of normal string to encoded query

    print("OPENING...")
    speak("Opening")

    wb.open(f"https://www.google.com/search?q={encoded_query}")         #google search

if (inp_med.lower() == "text"):         #operations in case of text input        

    print("YOU HAVE CHOOSEN TEXT INPUT AS A MEDIUM")
    speak("You have choosen text input as a medium")
    speak("Enter the text")
    command = input("GOOGLE SEARCH: ")

    print(f"YOU ENTERED, {command.upper()}")
    speak(f"You entered, {command}")

    encoded_query = urllib.parse.quote(command)
    print("OPENING...")
    speak("Opening")

    wb.open(f"https://www.google.com/search?q={encoded_query}")
    