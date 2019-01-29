"""
Wap to accept a file name and directory name from user and create a backup of this file in same directory
"""

import os

directory = raw_input("Enter a directory and file path name: ")
filename = raw_input("Enter a text file name: ")

if os.path.isdir(directory) and os.path.exists(directory+"\\"+filename+".txt"):
    f = open(filename+".txt")
    f1 = open(filename+"_bak.txt", "a")
    for x in f.readlines():
        f1.write(x)
    print "Backup successfully created."
    f.close()
    f1.close()
else:
    print "Path not find."
