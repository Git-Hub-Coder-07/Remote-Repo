import time
from assistant.speech_recognition import SpeechRecognizer
from assistant.text_to_speech import TextToSpeech
from assistant.commands import CommandHandler

def main():
    speech_recognizer = SpeechRecognizer()
    text_to_speech = TextToSpeech()
    command_handler = CommandHandler()

    text_to_speech.speak("Voice Assistant is now active. How can I assist you?")

    while True:
        command = speech_recognizer.listen()
        if command:
            response = command_handler.execute_command(command)
            text_to_speech.speak(response)
        time.sleep(1)

if __name__ == "__main__":
    main()