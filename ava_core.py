import speech_recognition as sr

from ava_cmds import *

# Read AVA's Configuration
import configparser
config = configparser.ConfigParser()
config.readfp(open(r'ava-config.conf'))

# Functions Start

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
            speak(e)
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
