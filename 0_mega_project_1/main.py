import speech_recognition as sr
import webbrowser as wb 
import pyttsx3
import musicLibrary
import requests
import time
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv

load_dotenv()


recognizer = sr.Recognizer()
# engine = pyttsx3.init('sapi5') 
newsapi = "43ca91ef2f4e4efa8cabbf05ea0ffd1b"

def speak_old(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    time.sleep(2)
    
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.get_busy():
        pygame.time.clock().tick(10)
        
    pygame.mixer.music.unload()
    # os.remove("temp.mp3")


def aiProcess(command):
    client = OpenAI(
    api_key= os.environ.get("open_api_key")
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system", "content": "you are a virtual assistant name soma skilled in general task like alexa and google cloud. give short responses please."
        },
        {
            "role":"user",
            "content":command
        }
        ]
    )   

    return completion.choices[0].message.content
    
    
    
def processCommand(c):
    if "open google" in c.lower():
        wb.open("https://google.com")
    elif "open facebook" in c.lower():
        wb.open("https://facebook.com")
    elif "open youtube" in c.lower():
        wb.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        wb.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        wb.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={os.environ.get("news_api_key")}")
        if r.status_code == 200:
            data = r.json()
            
            articles = data.get('articles',[])
            
            if not articles:
                speak("Sorry, no news articles found.")
            else:
                speak("Here are the top headlines.")
                for i, article in enumerate(articles[:5]):  # Limit to 5
                    title = article.get('title', 'No title available')
                    print(f"Headline {i+1}: {title}")
                    speak(title)
    else:
        #let open ai hendle the request
        output = aiProcess(c)
        speak(output)
        
    

if __name__ == "__main__":
    speak("Initializing Soma....")
    r = sr.Recognizer()
    
    # print("Testing speech engine...")
    # speak("Speech engine is working")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                # Give some buffer for speech
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=5, phrase_time_limit=3)

            word = r.recognize_google(audio).lower()
            print("Heard:", word)

            if "hello" in word:
                print("Soma Activated...")
                speak("Yes sir")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio).lower()
                    print("Command:", command)
                    processCommand(command)
            elif "exit" in word or "quit" in word:  # Fixed the exit condition
                speak("Goodbye sir")
                break 

        except sr.WaitTimeoutError:
            print("Timeout: no speech detected")
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error:", e)
