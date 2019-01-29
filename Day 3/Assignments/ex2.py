"""
Wap to accept directory name from user and remove all the empty files, from that directory. (os.path.getsize)
"""

import os
# import fnmatch
path = raw_input("Enter file name: ")
# print len(fnmatch.filter(os.listdir(path), '*.py'))
# cpt = ([files for r, d, files in os.walk(path) for fl in files if fl.endswith('.py')])
# print cpt
sum = 0
for root, dir, files in os.walk(path):
    for filename in files:
        fsize = os.path.getsize(root + "\\" + filename)
        if fsize <= 0:
            os.remove(root + "\\" + filename)
            print "File removed."
        else:
            print "No empty file found"
    break
