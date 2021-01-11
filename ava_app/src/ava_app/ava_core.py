import threading
from .ava_cmds import speak, questions, take_user_voice_in

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

def run_ava():
    #cloud = threading.Thread(target=cloud_sync, args=(), daemon=True)
    #cloud.start()
    voice_commands()

if __name__ == '__main__':
    run_ava()
