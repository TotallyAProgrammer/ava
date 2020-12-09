import pyttsx3
import speech_recognition as sr

from ava_cmds import *

# Read AVA's Configuration
import configparser
config = configparser.ConfigParser()
config.readfp(open(r'ava-config.conf'))

def speak(text):
    """
    The voice of AVA
    """
    # Initialize the engine
    engine = pyttsx3.init(driverName=None, debug=True)

    # Get and set female voice, because in this case Ava is a female.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Speak
    engine.say(text)

    # TODO Find and use a none blocking method so that commands can be cancelled
    # TODO Find a way to chose blocking and non-blocking based on circumstances. (Programmer choice? Automatic Choice?)
    # Blocking method! Process all queued TTS commands
    engine.runAndWait()

def checkInternetConnectivity():
    """
    Check if you're connected to the internet
    Returns True if connected, False if anything else
    """
    import requests
    try:
        requests.get("http://google.com")
        return True
    except:
        return False

def takeUserVoiceIn():
    """
    Get users voice and processes it
    """
    # Set up recognizer and source
    recog = sr.Recognizer()

    recog.dynamic_energy_threshold = True

    recog.pause_threshold = 0.8

    with sr.Microphone() as source:
        audio = recog.listen(source) # Blocking?

        # Start listening for data
        print("Listening...")

        try:
            print("Proccessing...")

            if checkInternetConnectivity():
                question = recog.recognize_wit(audio, str(config.get('SR', 'key')), False)
            else:
                question = recog.recognize_sphinx(audio, "en-US", None, None, None)
        except Exception as e:
            print(e)
            return "None"
    
    return question



def voice_commands():
    """
    Process commands
    """
    while True:
        query = takeUserVoiceIn().lower()
        if query == "None":
            print(query)
            pass
        else:
            print(query)
            #speak(query)
            pass

if __name__ == '__main__':
    # Run voice_commands
    voice_commands()
