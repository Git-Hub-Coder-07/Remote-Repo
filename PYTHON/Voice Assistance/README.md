# AI Voice Assistant

A Python-based voice assistant that can perform various tasks using voice commands.

## Features

- Voice recognition and text-to-speech capabilities
- Time and date information
- Wikipedia searches
- Web browser control
- Weather information
- Email sending
- Music playback
- Jokes
- And more!

## Prerequisites

- Python 3.7 or higher
- Microphone
- Internet connection
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone this repository or download the files

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. For Windows users, you might need to install PyAudio separately:
```bash
pip install pipwin
pipwin install pyaudio
```

4. Configure the following in the `voice_assistant.py` file:
   - Add your Gmail credentials for email functionality
   - Add your OpenWeatherMap API key for weather information
   - Set your music directory path

## Usage

1. Run the voice assistant:
```bash
python voice_assistant.py
```

2. Wait for the greeting message

3. Speak your command. Here are some example commands:
   - "What time is it?"
   - "What's today's date?"
   - "Search Wikipedia for [topic]"
   - "Open YouTube"
   - "Open Google"
   - "Play music"
   - "What's the weather in [city]?"
   - "Tell me a joke"
   - "Send email"
   - "Exit" or "Quit" to close the assistant

## Configuration

### Email Setup
1. Use a Gmail account
2. Enable 2-factor authentication
3. Generate an App Password
4. Update the email and password in the code

### Weather API
1. Sign up for a free API key at OpenWeatherMap
2. Add your API key to the code

## Troubleshooting

1. If you get a PyAudio installation error:
   - Windows: Use pipwin to install PyAudio
   - Linux: Install portaudio19-dev first
   - Mac: Install portaudio first

2. If the voice recognition is not working:
   - Check your microphone settings
   - Ensure you have an internet connection
   - Try speaking clearly and in a quiet environment

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 