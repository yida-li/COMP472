from socket import *

#initilization
serverSocket = socket(AF_INET, SOCK_STREAM)

#serverSocket.bind(('localhost', 12000))
serverSocket.bind(('', 12000))
serverSocket.listen(1)

while True:
    #waiting to accept connection
    connectedSocket, address = serverSocket.accept()
    message = connectedSocket.recv(1024)

    #get the name which should be coen366
    sourcename = message.decode('utf-8')
    #add .html to the name
    httpRequest = sourcename.split()[1]+".html"

    #returns object to be read
    f = open(httpRequest[1:])
    # or f = open("coen366.html")
    objectFile = f.read()
    outputHTML = objectFile.encode('utf-8')
    connectedSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
    connectedSocket.send(outputHTML)
    break








