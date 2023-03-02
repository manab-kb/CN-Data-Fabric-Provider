from socket import *
from threading import *
import os
import pickle

# Class containing member functions and variables for a multithreaded server implementation
class multithreadServer(object):
    # Constructor function to create a socket with the hostname and port number provided by the GCS
    def __init__(self, hostname, portnum):
        self.host = hostname
        self.port = portnum

        # Opening the created database for the blockchain
        self.dbname = "College Green.txt"
        os.chdir("C:/Users/Manab Kumar Biswas/CN-Data-Fabric-Provider/GCS")
        self.f = open(self.dbname, "a+")

        # Creation and binding a TCP soclet with socket options set to resue addresses once clients are disconnected
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    # Function which actively listens for UAVs(clients) to connect to the itself and creates threads for each connection from an UAV
    def listen(self):
        self.sock.listen(10)
        while True:
            client, add = self.sock.accept()
            Thread(target = self.recvData, args = (client,)).start()

    # Function which helps in receiving data from the UAV's (clients) - function to be executed by each running thread
    def recvData(self, client):
        blockData = ""
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    blockData = pickle.loads(data)
                    # Thread(target = self.f.writelines, args = (blockstrData,)).start() # Add code to make sure necessary lines are rewritten
                else:
                    # Possibility of UAV disconnection as data is not being received by the server
                    raise error("@log: possibility of UAV disconnection.")
                print(blockData)
                self.f.write(blockData)
                self.f.close()
            except:
                client.close()
                return False