#!/usr/local/bin/python
import threading
import socket

serverPort = 15080  #modify this port to your port number
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#These options should cause the port to become available
#soon after the server terminates
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((socket.gethostname(), serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")
while 1:
    (connectionSocket, addr) = serverSocket.accept()
    expression = connectionSocket.recv(1024)
    #need to modify this code so that the connection is handled 
    #in a thread
    connectionSocket.send("42".encode('utf-8'));
    connectionSocket.close()

