###################################################
# this code implements a basic blockchain program #
# creaton of actual blockchain called bac_chain   #
# author: and_bac 2019                            #
###################################################

import hashlib
import json
import datetime as date
from bac_blocks import Block 
import time

class Bac_Chain(): #these are the actual blocks used for the transactions and the creation of the bac_chain blockchain
    def __init__(self):
        self.chain=[self.genesis(),] # this is the definition of the chain of blocks [which is a list] that has the genesis block as first block as absolute block 0
                                     
    def genesis(self): #generation of the initial block of the chain
        return Block(0, "01/01/1970", "init_block_data", "")
    
    def last_block(self):
        return self.chain[-1] # defining the last object of the list as per python syntax

    def add_block(self, newBlock): #this is the function to add a new block
        newBlock.prev_hash=self.last_block().hash # the new block has a previous hash value that is the previous block's hash value
        newBlock.hash=newBlock.hash_calc() # this is calculating the current hash value of the block
        self.chain.append(newBlock) # this method is appending blocks after using the method append to add object at the end of the list

    def validate(self): #function to check the integrity of the chain
        for i in range(1, len(self.chain)):
            prev_block=self.chain[i-1]
            curr_block=self.chain[i]
            if (curr_block.hash != curr_block.hash_calc()):
                print ("invalid block")
                return False
            elif (curr_block.prev_hash != prev_block.hash):
                print ("invalid hash, so invalid chain")
                return False
        return True , print("well done mrbacco, your chain is a valid blockchain ")

bac = Bac_Chain() #new object from the Bac_Chain class


def chains(add = int(input("please enter the number of blocks to create the blockhain: "))):
    for i in range(1, add):
        bac.add_block(Block(1, date, 90879087))
        time.sleep(1)
    return i*add
'''
add_b = int(input("please enter the number of blocks you want to generate: "))
add_index = int(input("please enter the starting index number: "))
add_data = str(input("please enter the data for each block: "))

for i in range(1, add_b):
    bac.add_block(Block(add_index, date.datetime.now()))

bac.add_block(Block(1, date, 90879087))
time.sleep(1)
bac.add_block(Block(2, date, 9087))
time.sleep(1)
bac.add_block(Block(3, date, "pippo"))
time.sleep(1)
bac.add_block(Block(4, date, 66477))
time.sleep(1)
bac.add_block(Block(5, date, "ungabunga"))
time.sleep(1)
'''
#bac.chain[2].data = "pippo"
#bac.chain[2].hash = bac.chain[2].hash_calc()

'''
for i in range (100):
    bac = bac.add_block(i)
bac
'''
for n in bac.chain:
    print(n)
print(bac.validate())
