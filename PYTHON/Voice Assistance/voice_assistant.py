import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyjokes
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class VoiceAssistant:
    def __init__(self):
        # Initialize text-to-speech engine
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 190)

        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()

        # Set up email configuration (you'll need to add your email and password)
        self.email = "your_email@gmail.com"
        self.password = "your_app_password"  # Use app password for Gmail

    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen for voice commands"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.pause_threshold = 1
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            query = self.recognizer.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception as e:
            print("Say that again please...")
            return "None"

    def wish_me(self):
        """Greet the user based on time of day"""
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good Morning!")
        elif 12 <= hour < 18:
            self.speak("Good Afternoon!")
        else:
            self.speak("Good Evening!")
        self.speak("I am your voice assistant. How can I help you?")

    def get_time(self):
        """Get current time"""
        time = datetime.datetime.now().strftime("%H:%M")
        self.speak(f"The current time is {time}")

    def get_date(self):
        """Get current date"""
        date = datetime.datetime.now().strftime("%d %B %Y")
        self.speak(f"Today's date is {date}")

    def search_wikipedia(self, query):
        """Search Wikipedia"""
        self.speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        self.speak("According to Wikipedia")
        self.speak(results)

    def open_website(self, url):
        """Open a website"""
        webbrowser.open(url)

    def play_music(self):
        """Play music from a specified directory"""
        music_dir = "path_to_your_music_directory"  # Add your music directory path
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))

    def get_weather(self, city):
        """Get weather information (requires API key)"""
        api_key = "your_openweathermap_api_key"  # Add your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={api_key}&q={city}"
        response = requests.get(complete_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            temperature = main["temp"] - 273.15  # Convert to Celsius
            humidity = main["humidity"]
            weather_description = data["weather"][0]["description"]
            
            self.speak(f"Temperature is {temperature:.1f} degrees Celsius")
            self.speak(f"Humidity is {humidity} percent")
            self.speak(f"Weather is {weather_description}")
        else:
            self.speak("City not found")

    def send_email(self, to_email, subject, body):
        """Send an email"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, to_email, text)
            server.quit()
            self.speak("Email sent successfully")
        except Exception as e:
            self.speak("Sorry, I couldn't send the email")

    def tell_joke(self):
        """Tell a random joke"""
        joke = pyjokes.get_joke()
        self.speak(joke)

    def run(self):
        """Main function to run the voice assistant"""
        self.wish_me()
        
        while True:
            query = self.listen()

            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                self.search_wikipedia(query)
            
            elif 'open youtube' in query:
                self.speak("Opening YouTube")
                self.open_website("youtube.com")
            
            elif 'open google' in query:
                self.speak("Opening Google")
                self.open_website("google.com")
            
            elif 'time' in query:
                self.get_time()
            
            elif 'date' in query:
                self.get_date()
            
            elif 'play music' in query:
                self.play_music()
            
            elif 'weather' in query:
                self.speak("Which city?")
                city = self.listen()
                self.get_weather(city)
            
            elif 'joke' in query:
                self.tell_joke()
            
            elif 'send email' in query:
                try:
                    self.speak("What should I say?")
                    content = self.listen()
                    self.speak("To whom should I send?")
                    to_email = self.listen()
                    self.send_email(to_email, "Voice Assistant Email", content)
                except Exception as e:
                    self.speak("Sorry, I couldn't send the email")
            
            elif 'exit' in query or 'quit' in query or 'bye' in query:
                self.speak("Goodbye!")
                break

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run() 