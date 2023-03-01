from geopy import *
from datetime import *
from fuzzyhashlib import *

# Class containing member functions and variables for the blockchain
class Blockchain:

    # Constructor function to declare and initialize all member variables being used
    def __init__(self,  proof, hash, powlen, initLat = 53.344250, initLong = -6.262410,):
        if proof == hash == 0:
            # Creating an empty blockchain
            self.bchain = []

        # Tuple for coordinates from location coordinates entered by the user / default values
        self.initLat = initLat
        self.initLong = initLong
        self.coord = (self.initLat, self.initLong)

        # Declaring and initialising variables for proof, hash, prevhash and powlen
        self.proof = proof
        self.hash = hash
        self.prevhash = 0
        self.powlen = powlen

        # Determining name of location from coordinates - to name the centralised database
        self.geoloc = Nominatim(user_agent="blockchain_uavnet")
        self.locname = self.geoloc.reverse(str(self.coord))

    # Function to create and append a new block
    def createBlock(self):
        # New block is based on proof from the current UAV and hash values of the prev block
        if len(self.bchain) == 0:
            self.prevHash = 0
        else:
            tempblock = self.bchain[-1]
            self.prevHash = tempblock['hash']
        self.newBlock = {'index' : len(self.bchain) + 1, 'prevHash' : self.prevHash, 'hash' : self.hash, 'proof' : self.proof, 'timestamp' : str(datetime.now())}
        self.bchain.append(self.newBlock)

    # Function to calculate the hashvalue for the block
    def hashValue(self):
        hashVal = sdhash(self.newBlock).hexdigest()
        return hashVal

    # Function for Proof Of Work (POW)
    def poW(self, powcomp):
        # checking if the area covered by the UAV matches the defined area to be covered by the GCS
        if powcomp < self.powlen:
            print("@log: POW match failed: Covered area lesser than defined area.")
            return False
        else:
            return True

    # Function to validate each transaction of data within the blockchain
    def validate(self):
        block1 = self.bchain[0]
        blockind = 1

        # Checking if block indices and hash values are as needed
        while blockind < len(self.bchain):
            block2 = self.bchain[blockind]

            if self.hashValue(block1) != block2['prevHash']:
                print("@log: hashvalue mismatch.")
            
            else:
                continue