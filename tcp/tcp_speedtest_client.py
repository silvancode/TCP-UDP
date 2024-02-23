import socket
import time

# Einrichtung Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9999))
client.settimeout(5)  # Setzt ein timeout für client.recv()

# Nachricht
text = ('It is a truth universally acknowledged, that a single man '
        'in possession of a good fortune, must be in want of a wife. '
        'However little known the feelings or views of such a man '
        'may be on his first entering a neighbourhood, this truth is so '
        'well fixed in the minds of the surrounding families, '
        'that he is considered the rightful property of some one or other of '
        'their daughters. "My dear Mr. Bennet," said his lady to him one day, '
        '"have you heard that Netherfield Park is let at last?"  '
        'Mr. Bennet replied that he had not. "But it is," returned she; '
        '"for Mrs. Long has just been here, and she told me all about it." '
        'Mr. Bennet made no answer. "Do you not want to know who has taken it?" cried his wife impatiently. '
        '"YOU want to tell me, and I have no objection to hearing it." ... ')

start = time.time()

# Sendet 100 Nachrichten
for _ in range(100):

    # Empfängt und gibt Antwort aus
    try:
        data = client.recv(1024).decode('utf-8')
        print(f"Received from server: {data}")
        client.send(text.encode('utf-8'))
    except socket.timeout:
        print("Server did not respond within timeout")

# Testresultat
end = time.time()
print(f"Time taken: {end - start}")
client.close()
