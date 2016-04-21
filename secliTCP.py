import socket

ping=[0x4D,0x00,0x01,0x00,0x04,0xA3,0x06,0x21,0x08,0x50]

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('96.127.158.186', 58862))
clientsocket.send(bytearray(ping))
received = clientsocket.recv(1024)
clientsocket.close()  
print received
