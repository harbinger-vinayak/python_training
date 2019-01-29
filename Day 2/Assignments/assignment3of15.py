"""
Write a Python program to calculate product of digits of a number
"""

num = input("Enter a number: ")
str_ls = str(num)
ls = list(str_ls)
product = 1

for i in str_ls:
    product = product * int(i)

print "The Product of Digits is", product
