import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 9999))
server.settimeout(2)  # Set a timeout for recvfrom()

# Store received messages (consider a more efficient data structure if needed)
received_messages = []

while True:
    try:
        message, address = server.recvfrom(1024)
        received_messages.append(message.decode('utf-8'))

        # Send response immediately
        server.sendto(f"Hello Client! (Response to: {message.decode('utf-8')})".encode('utf-8'), address)

        # Print received messages periodically
        if len(received_messages) % 10 == 0:
            print(f"Received messages: {received_messages[-10:]}")

    except socket.timeout:
        print("No message received within timeout")

