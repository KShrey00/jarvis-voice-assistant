import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "<your news api>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


def processAI(command):
    client = OpenAI(
    api_key = "<your openai api"
    )

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages = [
            {"role" : "system", "content" : "you are a virtual assistant named Jarvis skilled in general tasks like alexa and gemini"},
            {"role" : "user", "content" : command}       
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        name = c.lower().split(" ").remove(0)
        link = musiclibrary.nusic[name]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the JSON response
            data = r.json()

            # extract the articles
            articles = data.get('articles',[])

            #speak the headlines
            for article in articles:
                speak(articles['title'])

    else:
        # let openAI handle the request
        output = processAI(c)
        speak(output)



if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word "Jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizing...")
        try:
            with sr.Microphone(device_index=0) as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if word.lower() == "jarvis":
                speak("Ya!")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print(f"Error; {e}")
