"""
Star pattern programs - Write a Python program to print the given star patterns
"""

num = int(raw_input("Enter a max number: "))
fill = '*'.center(2)
i = 1
while i <= num:
    print fill * i
    i += 1
