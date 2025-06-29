# Voice Assistant Project

This project is a fully functional voice assistant that can recognize speech, convert text to speech, and execute commands based on user input.

## Features

- Speech recognition to capture user commands.
- Text-to-speech functionality to respond to users.
- A command handler to manage and execute various commands.
- Utility functions for logging and error handling.

## Project Structure

```
voice-assistant
├── src
│   ├── main.py
│   ├── assistant
│   │   ├── __init__.py
│   │   ├── speech_recognition.py
│   │   ├── text_to_speech.py
│   │   ├── commands.py
│   │   └── utils.py
│   └── config
│       └── settings.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd voice-assistant
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the voice assistant, execute the following command:
```
python src/main.py
```

## Configuration

Configuration settings can be found in `src/config/settings.py`. Modify this file to set your API keys, language preferences, and other constants.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.

## License

This project is licensed under the MIT License. See the LICENSE file for details.