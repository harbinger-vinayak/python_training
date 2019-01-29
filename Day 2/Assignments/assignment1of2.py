"""
Write a Python program to print all natural numbers in reverse (from n to 1)
"""

n = int(input("Enter a natural number: "))
for i in range(n, 0, -1):
    print i,
