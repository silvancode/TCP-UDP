import socket

# Einrichtung Server
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))
server.settimeout(2)  # Setzt ein timeout für recvfrom()

# Speichert empfangene Nachrichten
received_messages = []

# Empfangsschlaufe
while True:
    try:
        message, address = server.recvfrom(1024)
        received_messages.append(message.decode('utf-8'))

        # Sendet direkt Antwort
        server.sendto(f"Hello Client! (Response to: {message.decode('utf-8')})".encode('utf-8'), address)

        # Gibt empfangene Nachricht periodisch aus
        if len(received_messages) % 10 == 0:
            print(f"Received messages: {received_messages[-10:]}")

    except socket.timeout:
        print("No message received within timeout")
