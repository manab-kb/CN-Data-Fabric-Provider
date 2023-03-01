from socket import *

# Specifying loopback address as hostname alongsides accepting port number
hostname = "127.0.0.1"
portnum = int(input("Port Number: "))

# Creating a TCP socket and using it to connect to the server socket
with socket(AF_INET, SOCK_STREAM) as skt:
    skt.connect((hostname, portnum))
    skt.sendall(b"Hello, world")
    data = skt.recv(1024)
