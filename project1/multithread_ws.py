import concurrent.futures
from socket import *
import time


def processing(connectionSocket):
    try:
        print("Open conne")
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        print("Close conn")
    except IOError:
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
        connectionSocket.close()

serverSocket = socket(AF_INET, SOCK_STREAM)

port = 5091
serverSocket.bind(("", port))
serverSocket.listen(1)

executor = concurrent.futures.ThreadPoolExecutor()

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    a = executor.submit(processing, connectionSocket)


