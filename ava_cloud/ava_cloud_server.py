import sys
import socket
import threading

server_version = 1

# Server binding

BIND_PORT = 25680
BIND_ADDR = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((BIND_ADDR, BIND_PORT))
except socket.error as exp:
    print("Binding failed. Error: " + str(msg[0]) + " Message " + msg[1])
    sys.exit()

s.listen(10)

print("Socket bound and server listening.")

# Server function set-up

def send_data(data, conn):
    """
    Simplify sending information to client
    """
    try:
        conn.send((data +"\n").encode())
        return True
    except:
        return False

def rx_client_data(con):
    data = conn.recv(1024)
    data = data.decode().lower().replace("\n", "")
    return data

def client_connection(client):
    """
    Give clients a thread and a place to operate.
    """

    send_data("AVA Cloud ready.", client)


while True:
    try:
        connection, client_addr = s.accept()
        print("Connected with " + client_addr[0] + ":" + str(client_addr[1]))
        client = threading.Thread(target=client_connection, args=(connection, client_addr[0]), daemon=True)
        client.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, stopping service...")
        s.close()
        sys.exit()
    except SystemExit:
        print("AVA Cloud Server shutting down...")
        s.close()
        sys.exit()