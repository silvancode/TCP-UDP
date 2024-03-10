import socket

# Einrichtung Server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('139.162.157.217', 222))

while True:
    # Empfangsschleife
    message, address = server.recvfrom(1024)
    # print(message.decode('utf-8'))
    server.sendto(message, address)
