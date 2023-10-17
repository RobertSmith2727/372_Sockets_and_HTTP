# code derived from:
# https://www.geeksforgeeks.org/python-binding-and-listening-with-sockets/
# https://www.pubnub.com/blog/socket-programming-in-python-client-server-p2p/

import socket
plug = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localHost = '127.0.0.1', 3000

data = b"HTTP/1.1 200 OK\r\n"\
 b"Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 b"<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

getter = "GET /HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
plug.bind(localHost)
plug.listen()
conn, address = plug.accept()
conn.send(data)
plug.close()
