import sys
import socket


def main(argv):
    address = argv[1]
    port = int(argv[2])
    path = argv[3]

    client_socket = socket.socket()  # instantiate
    client_socket.connect((address, port))  # connect to the server
    message = "GET /" + path + " HTTP/1.1"
    client_socket.send(message.encode())  # send message
    data = client_socket.recv(1024).decode()  # receive response
    print(data)


if __name__ == "__main__":
    main(sys.argv)



# main
# take in args from cl
# call open client

# in client()

# open client socket
# client connects to server
# send get request to server
# accept response
# display server response
# client takes in the server IP, address or host name, the port where server,
# the path at which the requested object is stored at the server.
