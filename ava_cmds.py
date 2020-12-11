"""
AVA's primary commands file
Located here are all of AVA's core commands
"""

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
    # TODO "AVA, add the phrase <PHRASE> to the question <QUESTION>""
    print(question)
