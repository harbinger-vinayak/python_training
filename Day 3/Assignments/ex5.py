"""
Wap to convert each n every word in upper case in file
"""

import os

path = raw_input("Enter file name: ")
if os.path.exists(path):
    filename = open(path)
    with filename as fn:
        for line in fn:
            print line.upper(),
else:
    print "File not find."
