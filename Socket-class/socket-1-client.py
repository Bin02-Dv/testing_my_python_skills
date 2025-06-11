# the client side..

import socket
import threading

def receive_message(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if not msg:
                break
            print(f"Server: {msg}")
        except:
            break

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

thread = threading.Thread(target=receive_message, args=(client,))
thread.start()

while True:
    msg = input()
    client.send(msg.encode())