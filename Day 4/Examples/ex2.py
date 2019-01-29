import os

dire = raw_input("Enter a path: ")

if os.path.isdir(dire):
    os.chdir(dire)
    for infile in os.listdir(dire):
        if os.path.isfile(infile):
            size = os.path.getsize(infile)
            if size == 0:
                print 'Removed file name is:', infile
                os.remove(infile)
else:
    print "It's not a directory"
