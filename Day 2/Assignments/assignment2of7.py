"""
Write a Python program to find sum of all even numbers between 1 to n.
"""

num = int(raw_input("Enter a natural number: "))
num_sum = 0

for i in range(0, num + 1, 2):
    num_sum += i

print "The sum is:", num_sum
