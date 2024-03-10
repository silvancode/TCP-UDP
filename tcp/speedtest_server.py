import socket
import time

# Einrichtung Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen()
server.settimeout(5)  # Setzt ein timeout für server.accept()

# Empfangsschlaufe
while True:
    try:
        client, address = server.accept()
        print(f"Connected to {address}")

        for _ in range(100):
            client.send("Hello Client!".encode('utf-8'))
            time.sleep(0.1)  # kurzes delay

            # Wartet auf antwort von Client
            client.settimeout(2)  # Setzt ein timeout für client.recv()
            try:
                response = client.recv(1024).decode('utf-8')
                print(f"Received from client: {response}")
            except socket.timeout:
                print("Client did not respond within timeout")

        client.close()

    except socket.timeout:
        print("No connection within timeout")
