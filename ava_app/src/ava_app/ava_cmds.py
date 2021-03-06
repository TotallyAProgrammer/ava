import configparser
import sys
import speech_recognition as sr
from .v_programmer import write_verbal_command, read_verbal_command
from .cmd_functions import cloud_server_version_retrieve, increment_ava_version
from .ava_connect_clouds import connect_ava_cloud, send_to_cloud

"""
AVA's primary commands file
Located here are all of AVA's core commands
"""

# Read AVA's Configuration
try:
    config = configparser.ConfigParser()
    config.read_file(open(r'C:\Users\foo\Documents\GitHub\ava\ava_app\src\ava_app\ava-config.conf'))
except Exception as exp:
    print(str(exp))
    sys.exit()

# Variables
cloud_mode = False
if config.get('MISC', 'force_offline').lower() == "true":
    inet_force_state = True
else:
    inet_force_state = False

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

def take_valid_input_in():
    """
    Waits for a valid user voice input
    """
    truth = True
    while truth == True:
        voice = take_user_voice_in()
        if voice is not None:
            truth = False
            return voice

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
    if inet_force_state == True:
        print("Offline mode is enabled")
        return False
    else:
        import requests
        try:
            requests.get("http://google.com")
            return True
        except requests.ConnectionError:
            return False

def q_proc(question=None, ava_cmd=None):
    return question == ava_cmd or read_verbal_command(question) == ava_cmd

def cloud_questions(socket, question=None):
    """
    Handle questions for cloud services
    socket = the cloud socket object
    question = the users question
    """
    question = str(question).lower()
    s = socket
    if q_proc(question, "ava cloud version"):
        return send_to_cloud(socket, "ava cloud version")
    elif q_proc(question, "ava cloud help"):
        return send_to_cloud(socket, "ava cloud help")



def questions(question=None):
    """
    AVA's main questions function
    """
    # Answer Arrays
    yes_answers = {"yes", "yeah", "yep", "yup", "okay", "ok"}
    no_answers  = {"no", "nope", "nah"}

    # Variables
    question = question.lower()
    ava_version = "130"
    global cloud_mode

    # Questions
    if cloud_mode != True:
        if question in {"ava add trigger", "hey add trigger", "eva add trigger"}: # Verbal Programmer
            speak("Okay. What is the trigger phrase?")
            t_phrase = take_valid_input_in()
            # speak(t_phrase)
            speak("Okay. What is the original command?")
            orig_cmd = take_valid_input_in()
            # speak(orig_cmd)
            speak("The new trigger command is: " + t_phrase + ", for the command " + orig_cmd + ". Is this correct?")
            answer = take_valid_input_in()
            if answer.lower() in yes_answers:
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
        elif q_proc(question, "ava what is your version"):
            speak("My version is " + ava_version + ". My cloud server is version " + cloud_server_version_retrieve())
        elif q_proc(question, "ava exit"):
            speak("Okay, exitting...")
            sys.exit()
        elif q_proc(question, "ava update version"):
            speak("Incrementing my version.")
            increment_ava_version()
            speak("Done.")
        elif q_proc(question, "ava cloud enable"):
            speak("Switching to cloud mode...")
            # global cloud_mode
            cloud_mode = True
        elif q_proc(question, "ava is cloud mode enabled"):
            speak("AVA Cloud mode is enabled.")
        print(question)
    elif cloud_mode == True:
        if q_proc(question, "ava is cloud mode enabled"):
            speak("AVA Cloud mode is enabled.")
        elif q_proc(question, "ava exit cloud mode"):
            speak("Exiting cloud mode")
            # global cloud_mode
            cloud_mode = False
        elif q_proc(question, "ava connect to ava cloud"):
            speak("Attempting to connect to AVA Cloud...")
            try:
                if check_internet_connectivity == True:
                    global ava_c_socket
                    ava_c_socket = connect_ava_cloud(str(config.get('AVA_CLOUD', 'ip')), str(config.get('AVA_CLOUD', 'port')))
                    ava_cloud_connect = True
                else:
                    raise "Offline mode is enable in the configuration file."
            except Exception as exp:
                speak("An error occured, would you like me to read it to you?")
                while True:
                    answer = take_valid_input_in()
                    if answer in yes_answers:
                        speak("Okay, here is the error.")
                        speak(str(exp))
                        break
                    elif answer in no_answers:
                        speak("Okay.")
                        break
