# code derived from:
# https://docs.python.org/3/howto/sockets.html
# https://www.internalpointers.com/post/making-http-requests-sockets-python
# https://hackernoon.com/resolving-typeerror-a-bytes-like-object-is-required-not-str-in-python
# code and comments derived from: Chapter 2.7 of course textbook

import socket
# creates client socket called plug
plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# initiates client/server connection
plug.connect(("gaia.cs.umass.edu", 80))

get = b"GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
# sends client get request to TCP connection
plug.sendall(get)
# receives characters sent by server
response = plug.recv(10000)
# closes the socket
plug.close()
# prints server message
print(response.decode())


