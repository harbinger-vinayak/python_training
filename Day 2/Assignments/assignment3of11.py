"""
Write a Python program to find first and last digit of a number
"""

num = int(raw_input("Enter a natural number: "))
print "First digit of natural number is", int(str(abs(num))[:1])

print "Last digit of natural number is", int(str(str(abs(num))[::-1])[:1])
