import socket


def main(udp_address, send_text):
    # Einrichtung Client
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.settimeout(5)  # Setzt ein timeout für client.recv()
    try:
        # Datenaustausch
        client.sendto(send_text.encode('utf-8'), (udp_address, 222))
        data = client.recvfrom(1024)[0].decode('utf-8')
        # print(f"Received from server per udp: {data}")
    except socket.timeout:
        print("Server did not respond within timeout")


if __name__ == "__main__":
    address = 'localhost'
    text = 'test'
    main(address, text)
