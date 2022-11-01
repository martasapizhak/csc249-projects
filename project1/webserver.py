from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)

# -------------
# Fill in start
# -------------
# Assign a port number
# Bind the socket to server address and server port
# Tell the socket to listen to at most 1 connection at a time
port = 50991
serverSocket.bind(("", port))
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
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    # -----------
    # Fill in end
    # -----------

    try:

        # -------------
        # Fill in start
        # -------------
        # Receive the request message from the client
        message = connectionSocket.recv(1024)
        print(message)
        # -----------
        # Fill in end
        # -----------

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:])

        # -------------
        # Fill in start
        # -------------
        # Store the entire contents of the requested file in a temporary buffer
        outputdata = f.read()
        # -----------
        # Fill in end
        # -----------

        # -------------
        # Fill in start
        # -------------
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
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
        # Send response message for file not found
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n", "UTF-8"))
        connectionSocket.close()

        # -----------
        # Fill in end
        # -----------

# serverSocket.close()
# sys.exit()  # Terminate the program after sending the corresponding data
