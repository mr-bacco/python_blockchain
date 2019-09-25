###################################################
# this code implements a basic blockchain program #
# creaton of blocks                               #
# author: and_bac 2019                            #
###################################################

import hashlib
import json
import datetime as date

class Block(): # generation of the class called Block, every block will be an instance of this class
    def __init__(self, nonce, timestamp, data, prev_hash = ''):
        self.nonce = nonce
        self.timestamp = str(date.datetime.now())
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_calc()

    def hash_calc(self):
        hash_block=json.dumps( #using the method jason.dumps that allows to serialize the objects in a json format
            {
                "nonce":self.nonce, 
                "timestamp": self.timestamp, 
                "data":self.data, 
                "prev_hash": self.prev_hash
            },
        ).encode()
        return hashlib.sha256(hash_block).hexdigest() # creation of the hash from the block parameters as defined in the class

    def __str__(self): # returning the string representation of the objects
        string="nonce: " +str(self.nonce) +"\n"
        string+="timestamp; " +str(self.timestamp) +"\n"
        string+="data: " +str(self.data) +"\n"
        string+="prev_hash: " +str(self.prev_hash) +"\n"
        string+="hash: " +str(self.hash) +"\n"
        return string

new_block = Block
print (new_block)
