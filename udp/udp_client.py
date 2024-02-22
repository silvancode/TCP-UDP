import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

start = time.time()
client.sendto("Hello Server!".encode('utf-8'), ("127.0.0.1", 9999))
print(client.recvfrom(1024)[0].decode('utf-8'))
end = time.time()
print(end - start)
