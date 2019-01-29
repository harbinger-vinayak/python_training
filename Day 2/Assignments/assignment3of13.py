"""
Write a Python program to swap first and last digits of a number
"""

num = input("Enter a number: ")
temp = list(str(num))
temp[0], temp[-1] = temp[-1], temp[0]

print "The swap digits are", ''.join(temp)

