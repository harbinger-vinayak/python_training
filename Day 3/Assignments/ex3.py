"""
Wap to find out total no of lines total no of words total no of characters in file
"""

import os

path = raw_input("Enter file name: ")
if os.path.exists(path):
    filename = open(path)
    with filename as infile:
        lines = 0
        words = 0
        characters = 0
        for line in infile:
            wordslist = line.split()
            lines += 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)
    print "Total number of lines in file:", lines
    print "Total number of words in file:", words
    print "Total number of characters in file:", characters
else:
    print "File not find"
