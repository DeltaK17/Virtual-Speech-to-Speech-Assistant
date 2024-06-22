import speech_recognition as sr
import pyttsx3
import os
from groq import Groq

# Set the Groq API key
groq_client = Groq(api_key="your_groq_api_key_here")

# Function to convert text to speech
def SpeakText(Command):
    engine = pyttsx3.init()
    engine.say(Command)
    engine.runAndWait()

# Initialize recognizer
r = sr.Recognizer()

# Function to record user's speech
def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Listening...")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except sr.UnknownValueError:
            print("Unknown error occurred")

# Function to send user's message to Groq for response
def send_to_groq(messages, model="llama3-8b-8192"):
    chat_completion = groq_client.chat.completions.create(
        messages=messages,
        model=model,
    )
    return chat_completion.choices[0].message.content

messages = []

# Main loop for conversation
while True:
    text = record_text()
    if text.lower() == "exit":
        SpeakText("Goodbye!")
        break
    messages.append({"role": "user", "content": text})
    completion = send_to_groq(messages)
    SpeakText(completion)
    print(completion)
    messages.append({"role": "assistant", "content": completion})
