import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import sys

# Initialize speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties for text-to-speech
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you repeat?")
        return take_command()  # Recursive call to retry
    except sr.RequestError:
        print("Sorry, my speech service is down. Please try again later.")
        return ""
    return command

# Function to execute commands
def run_jarvis():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'search' in command:
        search_term = command.replace('search', '')
        webbrowser.open_new_tab('https://www.google.com/search?q=' + search_term)
        speak('Here is what I found for ' + search_term)
    elif 'open' in command:
        app = command.replace('open', '').strip()
        os.startfile(app)
    elif 'quit' in command:
        speak('Goodbye!')
        sys.exit()
    else:
        speak('I am sorry, I did not understand that command.')

# Main program execution
if __name__ == "__main__":
    speak("Hello! I am Jarvis. How can I assist you today?")
    while True:
        run_jarvis()