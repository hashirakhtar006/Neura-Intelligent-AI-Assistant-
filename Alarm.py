import pyttsx3
import datetime
import os
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedtime = open('AlarmText.txt','rt')
time = extractedtime.read()  
time = str(time)
extractedtime.close()


deletedtime = open('AlarmText.txt','r+')
deletedtime.truncate(0)
deletedtime.close()



def ring(time):
    timeset = str(time)
    timenow = timeset.replace("jarvis","")
    timenow = timenow.replace("set an alarm","")
    timenow = timenow.replace(" and ",":")

    Alarmtime = str(timenow)
    print(Alarmtime)

    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == Alarmtime:
            speak("Alarm ringing , sir")
            os.startfile("iphone_alarm.mp3")
        elif currenttime + "00:00:30" == Alarmtime:
            exit()

ring(time)        
