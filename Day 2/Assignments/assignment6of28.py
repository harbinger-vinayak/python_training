"""
Write a Python program to print Fibonacci series up to n terms
"""
nterms = int(input("How many terms you want? "))
# first two terms
n1 = 0
n2 = 1
count = 2
# check if the number of terms is valid
if nterms <= 0:
    print "Please enter a positive integer"
elif nterms == 1:
    print "Fibonacci sequence:"
    print n1
else:
    print "Fibonacci sequence:"
    print n1, n2,
    while count < nterms:
        nth = n1 + n2
        print nth,
        # update values
        n1 = n2
        n2 = nth
        count += 1
