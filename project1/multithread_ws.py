import concurrent.futures
from socket import *


def processing(connectionSocket):
    try:
        # responsible for processing the request, communicating with the client and throwing error
        print("Open connection")
        message = connectionSocket.recv(1024)
        # take filename, which comes as a second element after the first and space
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        print("Close connection")
    except IOError:
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
# https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
port = 5091
serverSocket.bind(("", port))
serverSocket.listen(1)

executor = concurrent.futures.ThreadPoolExecutor()

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    a = executor.submit(processing, connectionSocket)
