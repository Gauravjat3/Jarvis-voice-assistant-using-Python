import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
from googlesearch import search

myName = 'Jarvis'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Corrected property name

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    speak(f'Hi, I am {myName}. How may I assist you?')

def hear_me():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print('you said : ',query)  # Return the recognized query if successful
    except sr.UnknownValueError:
        print('Unable to recognize, please repeat!')
        return 'None'
    except sr.RequestError:
        print('Could not request results from Google Speech Recognition service')
        return 'None'
    return query

if __name__ == "__main__":
    greetme()
    while True:
        query = hear_me().lower()
 
        if 'wikipedia'in query:
            query = query.replace ('wikipedia','')
            speak('searching wikipedia...')
            result = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open google'in query:
            webbrowser.open('google.com')
            break
        elif 'open instagram'in query:
            webbrowser.open('instagram.com')
            break
        elif 'open spotify'in query:
            webbrowser.open('spotify.com')
            break
        elif'cancel'in query:
            break
        else:
            search = 'https://www.google.com/search?q='+query
            webbrowser.open (search)
            speak('google search results')