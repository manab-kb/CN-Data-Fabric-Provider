from Blockchain.blockchain import *
from os import *

# Class containing member functions and variables for the Ground Control Station(GCS)
class GCS(Blockchain):

    # Constructor function to declare and initialise all member variables being used alongside calling the superclass
    def __init__(self):
        super.__init__(0, 0, 250)

        # Creating a database for the blockchain
        self.dbname = self.locname + ".txt"
        chdir("../GCS")
        self.f = open(self.dbname, "a+")

    # Function to update the global db as and when blocks are created
    def globalcdb(self):

        # TO DO - add code for decentralised server socket implementation with broadcast messages to invoke UAV's
        pass

