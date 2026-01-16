import webbrowser as wb
import subprocess as sb
import speech_recognition as sr
import urllib.parse

inp_med = input("ENTER THE INPUT MEDIUM(VOICE/TEXT): ")

if (inp_med.lower() == "voice"):
    print("YOU HAVE CHOOSEN VOICE INPUT AS A MEDIUM")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("NOW SPEAK...")
        audio = r.listen(source)

    print("YOU SAID,", r.recognize_google(audio).upper())

    command = r.recognize_google(audio).lower()

    encoded_query = urllib.parse.quote(command)

    print("OPENING...")

    wb.open(f"https://www.google.com/search?q={encoded_query}")

if (inp_med.lower() == "text"):

    print("YOU HAVE CHOOSEN TEXT INPUT AS A MEDIUM")
    command = input("GOOGLE SEARCH: ")

    encoded_query = urllib.parse.quote(command)
    print("OPENING...")
    wb.open(f"https://www.google.com/search?q={encoded_query}")
    
