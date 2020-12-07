import pyttsx3
import speech_recognition as sr
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
    # Blocking method! Process all queued TTS commands
    engine.runAndWait()

def takeUserVoiceIn():
    """
    Get users voice and processes it
    """
    # Set up recognizer and source
    recog = sr.Recognizer()
    source = sr.Microphone()

    recog.dynamic_energy_threshold = True

    recog.pause_threshold = 0.8
    audio = recog.listen(source) # Blocking?

    # Start listening for data
    print("Listening...")

    try:
        print("Proccessing...")

        question = recog.recognize_wit(audio, str(config.get('SR', 'key')), False)

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
        print(query)

if __name__ == '__main__':
    # Run voice_commands
    voice_commands()
