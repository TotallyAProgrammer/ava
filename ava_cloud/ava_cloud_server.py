import socket
import threading

server_version = 1
BIND_PORT = 25680
BIND_ADDR = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((BIND_ADDR, BIND_PORT))
except socket.error as exp:
    print("Binding failed. Error: " + str(msg[0]) + " Message " + msg[1])
    exit()

s.listen(10)

print("Socket bound and server ready.")
