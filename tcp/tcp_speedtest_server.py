import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9999))
server.listen()
server.settimeout(5)  # Set a timeout for server.accept()

while True:
    try:
        client, address = server.accept()
        print(f"Connected to {address}")

        for _ in range(100):
            client.send("Hello Client!".encode('utf-8'))
            time.sleep(0.1)  # Introduce a short delay

            # Wait for a response from the client
            client.settimeout(2)  # Set a timeout for client.recv()
            try:
                response = client.recv(1024).decode('utf-8')
                print(f"Received from client: {response}")
            except socket.timeout:
                print("Client did not respond within timeout")

        client.close()

    except socket.timeout:
        print("No connection within timeout")

