"""
Write a Python program to find sum of first and last digit of a number
"""

num = int(raw_input("Enter a natural number: "))
first_digit = int(str(abs(num))[:1])
last_digit = int(str(str(abs(num))[::-1])[:1])

print "Sum of first and last digit is", first_digit + last_digit
