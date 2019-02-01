"""
Wap to accept directory name from user and remove if it is modify 30days older and if size is 100kb
"""

import os
import time

path = raw_input("Enter file name: ")
for root, dir, files in os.walk(path):
    for filename in files:
        fsize = os.path.getsize(root + "\\" + filename)
        fday = os.stat(root + "\\" + filename).st_mtime
        now = time.time()

        if fsize <= 100 and fday < now - 30 * 86400:
            os.remove(root + "\\" + filename)
            print "File removed."
        else:
            print "No file found"
    break
