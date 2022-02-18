import speech_recognition as sr
import pyaudio
import pyttsx3
from gtts import gTTS
import playsound
import _tkinter
import webbrowser
import pyjokes
import time
import datetime
from ecapture import ecapture as ec
import os
import subprocess
import requests
import wolframalpha
import json
from spotify_local import SpotifyLocal
import keyboard


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#def speak(audio):
    #num=0
    #print(audio)
   # num += 1
   # response=gTTS(text=audio, lang='en')
   # file = str(num)+".mp3"
    #response.save(file)
    #playsound.playsound(file, True)
    #os.remove(file)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    elif hour >= 18 and hour < 23:
        speak("Good Evening")
    else: 
        speak("Dude, go to bed")

    ainame = ("Lopez")

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Hmmmm...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"
    return query.lower()


WAKE = "lopez"


# wishMe()
while True:    
    
    clear = lambda: os.system('cls')

# This Function will clean any
# command before execution of this python file
    clear()
    query = takeCommand()
    if query.count(WAKE) > 0:
        query = query.replace("lopez ", "")

        if "goodbye" in query or "bye" in query or "stop" in query:
            speak('OK, talk to you later')
            print('Goodbye')
            break
        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Opening Google")
            time.sleep(5)

        elif 'search' in query:
            query = query.replace("search for", "")
            query = query.replace("search", "")
            speak(f"searching for: {query}\n")
            webbrowser.open_new_tab("https://www.google.com.tr/search?q={}".format(query))
            time.sleep(5)

        elif 'wolfram alpha' in query:
            # speak('I can answer to computational and geographical questions and what question do you want to ask now')
            query = query.replace("ask wolfram alpha ", "")
            query = query.replace("wolfram alpha ", "")
            query = query.replace("wolframalpha ", "")
            question = query
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            
        elif 'email' in query:
            print('opening email')
            query = query.replace("email ", "")
            speak('Sure, what do you want it to say?')


        elif 'who are you' in query or 'what can you do' in query:
            speak('I am Lopez, an AI made to assist you online')

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Patrick")
            print("I was built by Patrick")

        elif 'sarcasm levels' in query:
            print("I have a queue light I can use when i'm joking if you like")
            speak("I have a queue light I can use when i'm joking if you like")
            query = takeCommand()
            if 'that would probably help' in query or 'that would help' in query or 'that would be good' in query:
                print("yea you can use it to find your way back to the ship after i blow you out the airlock")
                speak("yea you can use it to find your way back to the ship after i blow you out the airlock")
                    

        elif 'play song' in query or 'play the song' in query:
            query = query.replace("play song", "")
            query = query.replace("play the song", "")
            print(f"playing: {query}\n")
            url = webbrowser.open_new_tab("https://www.youtube.com.tr/search?q={}".format(query))
            time.sleep(5)

        elif 'open' in query:
            query = query.replace("open ", "")
            
            if 'stackoverflow' in query or 'stack overflow' in query:
                webbrowser.open_new_tab("https://stackoverflow.com/login")
                speak("opening stackoverflow")

            elif 'xbox' in query:
                subprocess.Popen("XboxPcApp.exe")
                speak("opening xbox app")

            elif 'gmail' in query or 'email' in query:
                speak("Google Mail open now")
                #subprocess.Popen("mail.exe") 

            elif 'youtube' in query:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")

            elif 'spotify' in query:
                subprocess.Popen("Spotify.exe")
                speak("Opening spotify")
            time.sleep(3)


        elif 'news' in query:
            news = webbrowser.open_new_tab("")
            speak('Here are some headlines')
            time.sleep(4)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "robo camera", "img.jpg")

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                currentHumidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))
            else:
                speak(" City Not Found ")

        elif 'joke' in query:
            joke = pyjokes.get_joke(language= 'en', category= 'all')
            print(joke)
            speak(joke)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 seconds")
            subprocess.call(["shutdown", "/h"])
        time.sleep(3)
            
            
                
        







