import socket

# Einrichtung Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))  # Verbindung

# Datenaustausch
client.send("Hello Server!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
