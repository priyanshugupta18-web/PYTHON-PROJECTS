import webbrowser as wb
import subprocess as sb
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("NOW SPEAK...")
    audio = r.listen(source)

print("YOU SAID,", r.recognize_google(audio).upper())

command = r.recognize_google(audio).lower()

if "open youtube" in command:
    print("OPENINNG YOUTUBE...")
    wb.open("https://youtube.com")
if "open whatsapp" in command:
    print("OPENING WHATSAPP")
    sb.Popen("whatsapp")
if "open notepad" in command:
    print("OPENING NOTEPAD")
    sb.Popen("notepad")



