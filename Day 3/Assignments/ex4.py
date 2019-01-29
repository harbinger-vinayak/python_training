"""
Wap to convert the content of files in reverse order
"""
import os

path = raw_input("Enter file name: ")
if os.path.exists(path):
    filename = open(path)
    with filename as fn:
        for line in reversed(list(fn)):
            print line.rstrip()
else:
    print "File not find."
