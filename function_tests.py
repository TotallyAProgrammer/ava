import threading
from cmd_functions import *

def prnt():
    import time
    while True:
        print("test")
        time.sleep(3)

cloud = threading.Thread(target=cloud_sync, args=(), daemon=True)
prnt  = threading.Thread(target=prnt, args=(), daemon=True)
cloud.start()
prnt.start()
while True:
    pass