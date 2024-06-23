import speech_recognition as sr
import pyttsx3
from groq import Groq

# Set the Groq API key
groq_client = Groq(api_key="your_groq_api_key_here")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to record user's speech
def record_text():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return ""

# Function to send user's message to Groq for response
def send_to_groq(messages, model="llama3-8b-8192"):
    response = groq_client.chat.completions.create(messages=messages, model=model)
    return response.choices[0].message.content

# Main loop for conversation
messages = []

while True:
    user_text = record_text()
    if user_text:
        if user_text.lower() == "exit":
            speak_text("Goodbye!")
            break
        messages.append({"role": "user", "content": user_text})
        response_text = send_to_groq(messages)
        speak_text(response_text)
        print(response_text)
        messages.append({"role": "assistant", "content": response_text})
