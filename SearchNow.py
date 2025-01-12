import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
import wikipedia as googleScrap

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening ..........")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        audio = r.listen(source, timeout=4, phrase_time_limit=8)
        print("Understanding .......")
        query = r.recognize_google(audio,language="en-US")
        print(f"You Said :{query}\n")

    except Exception as e:
        print("say That again")
        return "None"

    return query

query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def searchGoogle(query):
    if "google" in query:
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak(f"this is what I found on google for :{query}")

        try:
            pywhatkit.search(query)
            result = wikipedia.summary(query,sentences=1)
            speak(result)

        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results for your search. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("I couldn't find anything related to that query.")
        except Exception:
            speak("No speakable output available.")  

def searchYoutube(query):
    if "youtube" in query:
        speak(f"This is what I found for your search for :{query}")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, Sir")

def searchwikipedia(query):
    """Search Wikipedia, speak the first two sentences, and open the page in a browser."""
    if "wikipedia" in query:
        speak(f"Searching Wikipedia:{query}")
        query = query.replace("jarvis", "").replace("wikipedia search", "").replace("wikipedia", "").strip()
        
        try:
            # Get the page summary
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            # Open the Wikipedia page in the browser
            page = wikipedia.page(query)
            webbrowser.open(page.url)
        
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:5]  # Show the first 5 options
            speak("Your query is ambiguous. Here are some possible matches:")
            for option in options:
                print(option)
                speak(option)
            speak("Please refine your search.")
        
        except wikipedia.exceptions.PageError:
            speak("I couldn't find any page matching your query.")
        
        except Exception as e:
            speak(f"An error occurred: {e}")

def searchUni(query):
    if "people" in query:
        speak(f"opening website sir:{query}")
        web = "https://my.uopeople.edu/login/index.php" 
        webbrowser.open(web)
        speak("Done, Sir")




        
