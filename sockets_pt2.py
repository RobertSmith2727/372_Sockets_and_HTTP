# code derived from:
# https://docs.python.org/3/howto/sockets.html
# https://www.internalpointers.com/post/making-http-requests-sockets-python
# https://hackernoon.com/resolving-typeerror-a-bytes-like-object-is-required-not-str-in-python

import socket
plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "gaia.cs.umass.edu", 80
plug.connect(IP)
get = b"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
plug.sendall(get)

response = plug.recv(10000)

print(response.decode())


