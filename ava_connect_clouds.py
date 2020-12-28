import socket
from cmd_functions import is_ip_valid, is_port_valid

'''
A library that allows AVA to connect to various cloud services
'''


def connect_ava_cloud(ip, port=25680):
    """
    Connect to AVA Cloud and return its socket to the caller
    ip = AVA Cloud's IP Address
    port = AVA Cloud's Port (Optional, default is 25680)
    """
    if is_ip_valid(ip) and is_port_valid(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        data = s.recv(1024)
        print("Received: ", repr(data))
        return s
    else:
        return False
