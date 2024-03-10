import socket

# Einrichtung Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))

server.listen()

# Verbindungsschleife
while True:
    client, address = server.accept()
    print(f"Connected to {address}")
    print(client.recv(1024).decode('utf-8'))  # Datenaustausch
    client.send("Hello Client!".encode('utf-8'))
    client.close()
