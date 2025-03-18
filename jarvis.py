import speech_recognition as sr
import pyttsx3
import webbrowser
import requests
import openai
import os
import pygame
from gtts import gTTS

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""

def open_website(command):
    websites = {
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "youtube": "https://www.youtube.com",
        "linkedin": "https://www.linkedin.com"
    }
    for site in websites:
        if site in command:
            speak(f"Opening {site}")
            webbrowser.open(websites[site])
            return
    speak("Website not recognized.")

def fetch_news():
    api_key = ""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()
    articles = response.get("articles", [])[:5]
    if articles:
        speak("Here are the latest news headlines:")
        for article in articles:
            speak(article["title"])
    else:
        speak("No news found.")

def get_gpt_response(query):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": query}]
    )
    answer = response["choices"][0]["message"]["content"]
    speak(answer)

def main():
    speak("Initializing Jarvis...")
    while True:
        command = recognize_speech()
        if "jarvis" in command:
            speak("Ya")
            command = recognize_speech()
            if "open" in command:
                open_website(command)
            elif "news" in command:
                fetch_news()
            elif "exit" in command:
                speak("Goodbye!")
                break
            else:
                get_gpt_response(command)

if __name__ == "__main__":
    main()
