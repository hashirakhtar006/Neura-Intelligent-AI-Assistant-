import pyttsx3
import speech_recognition 
from GreetMe import greetMe
import pyaudio
import pyautogui
import keyboard
import os
from bs4 import BeautifulSoup
import requests
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening ..........")
        r.pause_threshold = 3
        r.energy_threshold = 300
        audio = r.listen(source,0,4)


    try:
        print("Understanding .......")
        query = r.recognize_google(audio,language="en-US")
        print(f"You Said :{query}\n")

    except Exception as e:
        print("say That again")
        return "None"

    return query

def alarm(query):
    timehere = open("AlarmText.txt",'a')
    timehere.write(query)
    timehere.close()
    os.startfile("Alarm.py")

if __name__ == "__main__":
    speak("Jarvis Activated, Tell me your task by just saying Jarvis")
    while True:
        query = takeCommand().lower()
        if 'jarvis' in query:
            greetMe()

            while True:
                query = takeCommand().lower()
                if "sleep" in query:
                    speak("Ok Sir, You can Call me AnyTime")
                    break
                
                elif "hello" in query:
                    speak("Hello Sir, how are you?")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k") 
                    speak("video Played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video Muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning Volume Up, sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning Volume Down, sirk")
                    volumedown()   
                           
                elif "i am fine" in query:
                    speak("that's Great, sir")

                elif "how are you" in query:
                    speak("perfect, Sir ")

                elif "thank you" in query:
                        speak("you welcome, sir")
                
                elif "open" in query:
                    from Dictapp import openwebquery
                    openwebquery(query)

                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchwikipedia
                    searchwikipedia(query)

                elif "people" in query:
                    from SearchNow import searchUni
                    searchUni(query) 
                
                elif "set an alarm" in query:
                    print("input time Example :- HH:MM:SS")
                    speak("set the alarm")
                    a = input("please tell the time:- ")
                    alarm(a)
                    speak("Done, Sir") 

                elif "calculate" in query:
                    from calculate import WolfRamAlpha
                    from calculate import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)
                    


                elif "temperature" in query:
                    search = "temperature in karachi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                   

                elif "weather" in query:
                    search = "weather in karachi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")  

                elif "news" in query:
                    from News import latestnews
                    latestnews()


                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%I:%M %p")
                    speak(f"Sir, the time is {strTime}")
                    
                elif "exit" in query:
                    speak("Main....so...raha...hoon...disturb..mat..karna")
                    exit()
                elif "remember" in query:
                    rememberMessage = query.replace("remember that",'')
                    rememberMessage = query.replace("jarvis",'')
                    speak(f"You told me" + {rememberMessage})
                    remember = open("remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("you told me" + remember.read())








