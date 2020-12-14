import configparser
import speech_recognition as sr
from v_programmer import write_verbal_command, read_verbal_command

"""
AVA's primary commands file
Located here are all of AVA's core commands
"""

# Read AVA's Configuration
config = configparser.ConfigParser()
config.readfp(open(r'ava-config.conf'))


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
            # speak(exep)
            return "None"
    return question

def speak(text=None):
    """
    The voice of AVA
    """

    import pyttsx3

    # Initialize the engine
    engine = pyttsx3.init(driverName=None, debug=True)

    # Get and set female voice, because in this case Ava is a female.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # Speak
    engine.say(text)

    # TODO Find and use a none blocking method so that commands can be cancelled
    # TODO Find a way to chose blocking and non-blocking based on circumstances.
    #      (Programmer choice? Automatic Choice?)
    # Blocking method! Process all queued TTS commands
    engine.runAndWait()

def check_internet_connectivity():
    """
    Check if you're connected to the internet
    Returns True if connected, False if anything else
    """
    import requests
    try:
        requests.get("http://google.com")
        return True
    except requests.ConnectionError:
        return False

def questions(question=None):
    """
    docstring
    """
    question = question.lower()
    if question in {"ava add trigger", "hey add trigger", "eva add trigger"}:
        speak("Okay. What is the trigger phrase?")
        t_phrase = None
        truth = True
        while truth == True:
            t_phrase = take_user_voice_in()
            if t_phrase is not None:
                truth = False
        # speak(t_phrase)
        speak("Okay. What is the original command?")
        truth = True
        while truth == True:
            orig_cmd = take_user_voice_in()
            if orig_cmd is not None:
                truth = False
        # speak(orig_cmd)
        speak("The new trigger command is: " + t_phrase + ", for the command " + orig_cmd + ". Is this correct?")
        truth = True
        while truth == True:
            answer = take_user_voice_in()
            if answer is not None:
                if answer.lower() in {"yes", "yeah", "yep", "yup", "okay"}:
                    speak("Writing to persistent database")
                    try:
                        write_verbal_command(t_phrase, orig_cmd)
                        speak("Write successful")
                        return True
                    except:
                        speak("Unable to write to file")
                        return False
                else:
                    speak("Cancelling operation")
                    return False
    print(question)
