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

def is_ip_valid(ip):
    from ipaddress import ip_address
    try:
        ip_address(ip)
        return True
    except Exception as exp:
        return False
        
def is_port_valid(port):
    if 0 < int(port) and int(port) < 65536:
        return True
    else:
        return False

def cloud_sync():
    import time
    while True:
        print("syncing")
        time.sleep(60)