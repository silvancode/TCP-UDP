import time
import tcp_client
import udp_client
import os

repeat = 100
start = time.time()
server_frankfurt = "139.162.157.217"
server_tokyo = "172.105.209.177"
benchmark_server = server_tokyo

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

for _ in range(repeat):
    tcp_client.main(benchmark_server, text)
end = time.time()
print(f"TCP Time taken: {end - start}")

start = time.time()
for _ in range(repeat):
    udp_client.main(benchmark_server, text)
end = time.time()
print(f"UDP Time taken: {end - start}")


