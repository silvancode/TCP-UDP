import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))

start = time.time()
client.send("Hello Server!".encode('utf-8'))
print(client.recv(1024).decode('utf-8'))
end = time.time()
print(end - start)
