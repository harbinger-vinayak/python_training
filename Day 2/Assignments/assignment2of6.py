"""
Write a Python program to find sum of all natural numbers between 1 to n
"""

num = int(raw_input("Enter a natural number: "))
i = 1
sum = 0
while i <= num:
    print i,
    sum += i
    i += 1

print "\nSum of 1 to %d is %d" % (num, sum)
