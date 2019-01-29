"""
Write a Python program to calculate sum of digits of a number
"""

num = input("Enter a number: ")
sum = 0

for i in str(num):
    sum += int(i)

print "The sum of digits of number is", sum
