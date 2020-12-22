import sys
import socket
import threading
from ava_cloud_cmds import ser_ver, parse_questions

server_version = ser_ver()

# Server binding

BIND_PORT = 25680
BIND_ADDR = "0.0.0.0"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((BIND_ADDR, BIND_PORT))
except socket.error as exp:
    print("Binding failed. Error: " + str(exp))
    sys.exit()

s.listen(10)

print("Socket bound and server listening.")

# Server function set-up

def send_data(data, conn):
    """
    Simplify sending information to client or disconnect the client if requested
    """
    try:
        if data == "!!!DISCONNECT_CLIENT!!!":
            return data
        else:
            if data is not None:
                conn.send((data +"\n").encode())
                return True
            else:
                return True
    except Exception as exp:
        print("Message sending failed. Error: " + str(exp))
        return False

def rx_client_data(conn):
    data = conn.recv(1024)
    data = data.decode().lower().replace("\n", "")
    return data

def client_connection(client, client_addr):
    """
    Give clients a thread and a place to operate.
    """

    send_data("AVA Cloud ready.", client)
    while True:
        recv = rx_client_data(client)
        #send_data(recv, client)
        msg_state = send_data(parse_questions(recv), client)
        if msg_state == "!!!DISCONNECT_CLIENT!!!":
            client.close()
            print("Client " + client_addr[0] + ":" + str(client_addr[1]) + " Disconnected!")
            break
        elif msg_state == False:
            print("Something went wrong... Possible issue with client thread!")



while True:
    try:
        connection, client_addr = s.accept()
        print("Connected with " + client_addr[0] + ":" + str(client_addr[1]))
        client = threading.Thread(target=client_connection, args=(connection, client_addr), daemon=True)
        client.start()
    except KeyboardInterrupt:
        print("KeyboardInterrupt detected, stopping service...")
        s.close()
        sys.exit()
    except SystemExit:
        print("AVA Cloud Server shutting down...")
        s.close()
        sys.exit()
