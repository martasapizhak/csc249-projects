from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------

# TODO: Assign a port number
#       Bind the socket to server address and server port
#       Tell the socket to listen to at most 1 connection at a time
serverSocket.bind(('0.0.0.0', 6793))
serverSocket.listen(1)

# -----------
# Fill in end
# -----------

while True:

    # Establish the connection
    print('Ready to serve...')

    # -------------
    # Fill in start
    # -------------
    connectionSocket, addr = serverSocket.accept()  # TODO: Set up a new connection from the client
    print(addr)
    # -----------
    # Fill in end
    # -----------

    try:

        # -------------
        # Fill in start
        # -------------
        message = connectionSocket.recv(1024)  # TODO: Receive the request message from the client
        print(message)
        # -----------
        # Fill in end
        # -----------

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        print(filename)
        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:])

        # -------------
        # Fill in start
        # -------------
        outputdata = f.read()  # TODO: Store the entire contents of the requested file in a temporary buffer
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------
        # TODO: Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK'.encode())
        # -----------
        # Fill in end
        # -----------

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()

    except IOError:

        # -------------
        # Fill in start
        # -------------
        connectionSocket.send('file not found'.encode())
        connectionSocket.close()
# TODO: Send response message for file not found
#       Close client socket
# -----------
# Fill in end
# -----------

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
