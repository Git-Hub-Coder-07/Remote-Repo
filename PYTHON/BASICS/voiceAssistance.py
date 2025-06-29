import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import sys

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-US')
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not get that.")
        speak("Sorry, I did not get that. Please say that again.")
        return ""
    except sr.RequestError:
        print("Sorry, the speech service is down.")
        speak("Sorry, the speech service is down")
        return ""

    return command.lower()

def respond(command):
    if 'hello' in command or 'hi' in command:
        speak("Hello! How can I help you today?")
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {now}")
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'search for' in command:
        search_term = command.split('search for')[-1].strip()
        if search_term:
            speak(f"Searching for {search_term}")
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
        else:
            speak("Please tell me what to search for.")
    elif 'exit' in command or 'quit' in command or 'stop' in command:
        speak("Goodbye!")
        sys.exit()
    else:
        speak("Sorry, I can not perform that task yet.")

def main():
    speak("Voice assistant activated. How can I help you?")
    while True:
        command = listen_command()
        if command:
            respond(command)

if __name__ == "__main__":
    main()

# Requirements:
# pip install SpeechRecognition pyttsx3 pyaudio
#
# On some systems, installing pyaudio may require additional steps.
# For Windows: you can use precompiled binaries from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# For Mac/Linux, install portaudio via package manager before installing pyaudio.

