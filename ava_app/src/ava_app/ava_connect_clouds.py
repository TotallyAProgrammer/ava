import socket
from .cmd_functions import is_ip_valid, is_port_valid

'''
A library that allows AVA to connect to various cloud services
'''

def send_to_cloud(socket, data):
    """
    Send data over the specified socket to the associated cloud
    socket = any socket object
    data = a string or int to be sent over the specified socket
    """
    try:
        data = data.encode()
        socket.send((str(data) +"\n").encode())
        return True
    except Exception as exp:
        print("Exception: " + str(exp))
        return False

def connect_ava_cloud(ip, port=25680):
    """
    Connect to AVA Cloud and return prepared socket to the caller
    ip = AVA Cloud's IP Address
    port = AVA Cloud's Port (Optional, default is 25680)
    """
    if is_ip_valid(ip) and is_port_valid(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        data = s.recv(1024)
        print("Received: ", repr(data))
        return s
    else:
        return False
