import configparser
from ava_cmds import speak, questions, check_internet_connectivity
import speech_recognition as sr

# Read AVA's Configuration
config = configparser.ConfigParser()
config.readfp(open(r'ava-config.conf'))



# Functions Start

def take_user_voice_in():
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

            if check_internet_connectivity():
                question = recog.recognize_wit(audio, str(config.get('SR', 'key')), False)
            else:
                question = recog.recognize_sphinx(audio, "en-US", None, None, None)
        except Exception as exep:
            print(exep)
            speak(exep)
            return "None"
    return question



def voice_commands():
    """
    Process commands
    """
    while True:
        query = take_user_voice_in().lower()
        if query == "None":
            #print(query)
            pass
        else:
            print(query)
            questions(query)
            #speak(query)

if __name__ == '__main__':
    # Run voice_commands
    voice_commands()
