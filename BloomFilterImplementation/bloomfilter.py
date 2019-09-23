# -----------------------------------------------------------------------
# CS 370
# bloomFilter.py
# Shreyans Khunteta
# Reference: http://www.maxburstein.com/blog/creating-a-simple-bloom-filter/
# -----------------------------------------------------------------------
 


BIT_ARRAY_SIZE  = 8964670
DICTIONARY_SIZE = 623517


open('output3.txt', 'w').close()    #removes data from previous runs
open('output5.txt', 'w').close()

from bitarray import bitarray
import mmh3
import sys
# To import all this, run below commands
# sudo pip install bitarray
# sudo pip install mmh3
import time
start_time = time.time()

class BloomFilter(object):
   #Here we implement the bloom filter.
   #We initialise it with values of self, size and number of hashes.
    def __init__(self, size, numHash):
    #Set the size of the bitarray to 8964670.
        self.numHash = numHash
        self.size = size
        self.bitarray = bitarray(size)
        self.bitarray.setall(0)

    # Add to ourBloomFilter mmh3 hashed with seed mod size
    def add(self, password):
        for seed in range(self.numHash):
            result = mmh3.hash(password, seed) % self.size
            self.bitarray[result] = 1

	# Check if read in is correct password
	# Or a false positive.
    def search(self, password):
        for seed in range(self.numHash):
            result = mmh3.hash(password, seed) % self.size
            if self.bitarray[result] == 1:
            	return "maybe"
            else:
            	return "no"


# createBF takes in the number of hashes, the input file, and the output file.
def createBF(numHash, inputFile, outputFile):
    ourBloomFilter = BloomFilter(BIT_ARRAY_SIZE, numHash)

     #Read in dictionary
     #Add what is read in to ourBloomFilter, mmh3 hashed with seed mod size
    dictionary = open('dictionary.txt').read().splitlines()
    for password in dictionary:
        ourBloomFilter.add(password)

    # Search ourBloomFilter and write to output file
    output = open(outputFile, 'w+')
    for password in inputFile:
        output.write(ourBloomFilter.search(password) + '\n')

def main():

    # Read in input passwords and pop first element (number of passwords)
	inputFile = open('sample_input.txt').read().splitlines()
	inputFile.pop(0)

    # Create bloom filters of numHash 3 and 5
    # start_time set to begin calculating how long calculating numHash of 3 will be.
	createBF(3, inputFile, 'output3.txt')
	print("ourBloomFilter with three hashes took %s seconds ---" % (time.time() - start_time))
	# Repeat process with numHash of 5.
	
	createBF(5, inputFile, 'output5.txt')
	print("ourBloomFilter with five hashes took %s seconds ---" % (time.time() - start_time))
	print "That's all folks."

if __name__ == "__main__": main()			
			