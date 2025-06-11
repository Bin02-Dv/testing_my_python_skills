# Creating the server
import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            print(f"Client: {msg}")
        except:
            break
    
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen(1)
print("[*] Waiting for connection...")

client_socket, addr = server.accept()
print(f"[+] Connected to {addr}")

thread = threading.Thread(target=handle_client, args=(client_socket,))
thread.start()

while True:
    msg = input()
    client_socket.send(msg.encode())