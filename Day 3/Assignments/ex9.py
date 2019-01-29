"""
Wap to find out count of all the python files in any specific directory and subdirectory
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
        if filename.endswith('.py'):
            sum += 1
print "Total number of .py files:", sum
