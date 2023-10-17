# code derived from:
# https://www.geeksforgeeks.org/python-binding-and-listening-with-sockets/
# https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/
# code and comments derived from: Chapter 2.7 of course textbook

import socket

# creates client socket called plug
plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# creates
localHost = '127.0.0.1', 3000

data = b"HTTP/1.1 200 OK\r\n"\
 b"Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 b"<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

getter = "GET /HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
# opens the socket
plug.bind(localHost)
# lets server listen for connection request
plug.listen()
# the client initiates the accept and creates "plug" as the socket
connection, address = plug.accept()
# receives and saves the connection response
response = connection.recv(10000)
# prints the connection response
print(response.decode())
# sends the message saved as "data"
connection.send(data)
# prints the message
print(data)
# closes connection
plug.close()



