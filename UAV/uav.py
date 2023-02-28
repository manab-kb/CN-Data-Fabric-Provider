from Blockchain.blockchain import *
from random import *
from math import *
from os import *

# Class containing member functions and variables for each individual UAV (Unmanned Aerial Vehicle - Drone)
class UAV(Blockchain):

    # Constructor function to declare and initialise all member variables being used alongside calling the superclass
    def __init__(self):
        self.lastBlock = self.bchain[-1]

        # Declaring and initializing variables to be used to compute proof for POW
        templat = self.initLat
        templong = self.initLong
        proof = 0
        dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))

        # Producing a random variable out of 4 choices to determine the direction amongst 4-axis in which the drone will navigate in order to cover all possible areas from the initial coordinates
        choice = randint(0,3)
        if choice == 0:
            # For each choice, checking if POW is completed. If not, incremental changes in coordinates are made and are tested again.
            while self.poW(dist) == False:
                templat += 0.00500
                templong += 0.00500
                proof += 1
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        if choice == 1:
            while self.poW(dist) == False:
                templat -= 0.00500
                templong += 0.00500
                proof += 2
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        if choice == 2:
            while self.poW(dist) == False:
                templat -= 0.00500
                templong -= 0.00500
                proof += 3
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        if choice == 3:
            while self.poW(dist) == False:
                templat += 0.00500
                templong -= 0.00500
                proof += 4
                dist = sqrt(pow((templat - self.initLat), 2) + pow((templong - self.initLong), 2))
        
        # Finding hashvalue for the block to be added and calling the functions to create and validate the block before being added into the blockchain
        hashv = self.hashValue()
        super.__init__(proof, hashv, 250)
        self.createBlock()
        self.validate()

    def globalcdb(self):
        # TO DO - add client socket code to communicate with other client sockets (decentralised) without the gcs and also with the gcs
        # Also add code to switch to local buffers only when UAV is disconnected from blockchain and match and update central blockchain db once connection is reestablished
        # Ensure GBN / SR and Timeouts are used to make the client code reliable
        # Also ensure UAV continues to run after one unit of proof has been generated (reset statistics)
        # Finally, also include coordinates for the drone in each block communication such that the location of the drone can be traced at any given point in time (useful when drone disconnects to find last active location)
        pass

    # Function used to switch creating blocks into the local buffer of each UAV when it disconnects from the central DB / Blockchain network
    def localBuff(self):
        # Creating a local db for the UAV if it already doesnt exist
        index = self.lastBlock['index']
        dirname = "UAV" + str(index)
        chdir("../UAV")
        if not path.exists(dirname):
            mkdir(dirname)
        chdir(dirname)

        # Continuing to write to the local db unless connection is established
        f = open("localBChain.txt" , "a+")
        f.writeline(self.bchain)
