import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('96.127.158.186', 58862))
clientsocket.close()  
