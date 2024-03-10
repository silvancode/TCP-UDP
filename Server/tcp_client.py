import socket


def main(tcp_address, send_text):
    # Einrichtung Client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((tcp_address, 111))
    client.settimeout(5)  # Setzt ein timeout für client.recv()
    try:
        client.send(send_text.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        # print(f"Received from server per tcp: {data}")
    except socket.timeout:
        print("Server did not respond within timeout")
    client.close()


if __name__ == "__main__":
    address = 'localhost'
    text = 'test'
    main(address, text)
