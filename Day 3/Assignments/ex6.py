"""
Find count of each and every word in file
"""

import os

path = raw_input("Enter file name: ")
if os.path.exists(path):
    filename = open(path)
    with filename as infile:
        words = 0
        for line in infile:
            wordslist = line.split()
            words = words + len(wordslist)
    print "Total number of words in file:", words
else:
    print "File not find"
