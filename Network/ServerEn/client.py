from socket import *

# Class containing member functions and variables for implementation of a client
class client:
    def __init__(self, hostname, portnum):
        # Specifying loopback address as hostname alongsides accepting port number
        self.host = hostname
        self.port = portnum
    
    def connect(self):
        # Creating a TCP socket and using it to connect to the server socket
        with socket(AF_INET, SOCK_STREAM) as skt:
            skt.connect((self.host, self.port))
            # Add code for sending blockchain data to the server (inheritance from blockchain)
            skt.sendall(b"@log: client connected to server")
            data = skt.recv(1024)
