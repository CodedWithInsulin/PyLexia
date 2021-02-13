# author and license
__author__ = "Coded With Insulin"
__license__ = "(GNU) gnu lesser general public license v2.1" + \
              "LINK: https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html"

# imports
import speech_recognition as sr
import pyttsx3
import pyjokes
import webbrowser
import pywhatkit
import tweepy
import pyowm
import os

# Import from "API.py"
from API import Open_Weather_API

from API import CONSUMER_KEY
from API import CONSUMER_SECRET
from API import ACCSES_TOKEN_KEY
from API import ACCSES_TOKEN_SECRET

# build importert stuff.
listener = sr.Recognizer()
mic = sr.Microphone()

# Build Lexia voice and such.
lexia = pyttsx3.init()
# change voice, rate and volume
rate = lexia.getProperty('rate')
volume = lexia.getProperty('volume')
voice = lexia.getProperty('voice')

# speed
newVoiceRate = 135
lexia.setProperty('rate', newVoiceRate)
lexia.runAndWait()

# volume
newVolume = 1.5
lexia.setProperty('volume', newVolume)
lexia.runAndWait()


def get_weather(command):
    home = 'Swifterbant, Netherlands'
    owm = pyowm.OWM(Open_Weather_API)
    mgr = owm.weather_manager()
    if "now" in command:
        observation = mgr.weather_at_place(home)
        w = observation.weather
        temp = w.temperature('Celsius')
        status = w.detailed_status
        talk("It is currently " + str(int(temp['temp'])) + " degrees and " + status)
    else:
        pass


def welcome_message():
    lexia.say("What can i do for you?")
    lexia.runAndWait()


def talk(text):
    lexia.say(text)
    lexia.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            welcome_message()
            print("speak now!")
            voicing = listener.listen(source)
            command = listener.recognize_google(voicing)
            command = command.lower()
            if "lexia" in command:
                command = command.replace("lexia", "")
    except:
        pass
    return command


def run_lexia():
    command = take_command()
    print(command)

    if command == "introduce yourself":
        talk("I am lexia. I'm a artificial intelligence.")

    elif "weather" in command:
        get_weather(command)

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "test tweet" in command:
        # authenticate to Twitter
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCSES_TOKEN_KEY, ACCSES_TOKEN_SECRET)

        # create API object
        api = tweepy.API(auth)

        # create a tweet
        api.update_status("test tweet")

    elif "open youtube" in command:
        talk("Opening YouTube.")
        webbrowser.open("https://www.youtube.com/")

    elif "open twitch" in command:
        talk("Opening Twitch.")
        webbrowser.open("https://www.twitch.tv")

    elif "open google" in command:
        talk("Opening Google.")
        webbrowser.open("https://www.google.com")

    elif "open facebook" in command:
        talk("Opening Facebook.")
        webbrowser.open("https://www.facebook.com")

    elif "open github" in command:
        talk("Opening github.")
        webbrowser.open("https://github.com")

    elif "open documents folder" in command:
        talk("Opening Documents.")
        os.startfile("C:/Users/Rondy/Documents")

    elif "open downloads folder" in command:
        talk("Opening downloads folder.")
        os.startfile("C:/Users/Rondy/Downloads")

    elif "stop" in command:
        quit()

    else:
        talk("I don't know how to do that yet.")


while True:
    run_lexia()
