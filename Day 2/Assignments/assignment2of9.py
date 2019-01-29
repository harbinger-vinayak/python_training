"""
Write a Python program to print multiplication table of any number
"""

num = int(raw_input("Enter a natural number: "))
i = 1
while i <= 10:
    print num, 'x', i, '=', num * i
    i += 1

