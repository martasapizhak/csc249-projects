import sys
import socket


def main(argv):
    # take in args from cl
    # client takes in the (server IP, address or host name), the port where server,
    # the path at which the requested object is stored at the server.
    address = argv[1]
    port = int(argv[2])
    path = argv[3]

    # https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

    client_socket = socket.socket()  # open client socket
    client_socket.connect((address, port))  # client connects to server
    message = "GET /" + path + " HTTP/1.1"  # create a request string
    client_socket.send(message.encode())  # send get request to server
    data = client_socket.recv(1024).decode()  # accept response
    print(data)  # display server response


if __name__ == "__main__":
    main(sys.argv)

