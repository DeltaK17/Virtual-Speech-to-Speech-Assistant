# Virtual-Speech-to-Speech-Assistant


This project is a speech-to-speech AI assistant that listens to your voice commands, processes them using the Groq AI API, and responds with synthesized speech. The assistant utilizes `speech_recognition` for converting speech to text and `pyttsx3` for converting text to speech.

## Features

- **Voice Command Recognition**: Listens to and recognizes your voice commands.
- **AI Response Generation**: Uses Groq's AI model to generate responses.
- **Speech Synthesis**: Converts AI-generated responses to speech.
- **Exit Command**: Gracefully exits the conversation loop when the user says "exit".

## Requirements

- Python 3.6+
- `speech_recognition`
- `pyttsx3`
- `groq` (Groq API client)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/speech-to-speech-ai-assistant.git
    cd Virtual-Speech-to-Speech-Assistant
    ```

2. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt`, create one with the following content:

    ```txt
    SpeechRecognition
    pyttsx3
    groq
    ```

3. **Set up your Groq API key**:

    Replace `"your_groq_api_key_here"` in the script with your actual Groq API key.

## Usage

Run the script to start the speech-to-speech AI assistant:

```sh
python Virtual-Speech-to-Speech-Assistant.py
