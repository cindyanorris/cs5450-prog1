#!/usr/local/bin/python

from socket import *

serverName = "student.cs.appstate.edu"
serverPort = 15080    #change this to the port assigned to you
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#modify this code so that it loops
sentence = input("Input expression to evaluate or quit to exit: ")
clientSocket.send(sentence.encode('utf-8'))
result = clientSocket.recv(1024);
print("The answer is ", result.decode());
clientSocket.close()

