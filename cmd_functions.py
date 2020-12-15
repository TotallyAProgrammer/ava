"""
Functions to slim down command code size
"""

def cloud_server_version_retrieve():
    """
    Retrieve AVA's cloud server version
    """
    return "0"

def increment_ava_version():
    """
    Increment AVA's version
    """
    try:
        with open('ava_version', 'r') as input_file:
            version = input_file.readline(1)
    except:
        pass
    with open('ava_version', 'a') as output:
        version = version + 1
        output.write(str(version))

def cloud_sync():
    import time
    while True:
        print("syncing")
        time.sleep(60)