import socket

# Einrichtung Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('139.162.157.217', 111))

server.listen()
# Verbindungsschleife
while True:
    client, address = server.accept()
    text = client.recv(1024)
    client.send(text)
    client.close()
