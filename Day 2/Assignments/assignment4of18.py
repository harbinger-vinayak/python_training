"""
Write a Python program to find frequency of each digit in a given integer
"""


def frequencydigits(n, d):
    c = 0
    while n > 0:
        # check for equality
        if n % 10 == d:
            c += 1
        # reduce the number
        n = int(n / 10)
    return c


number = int(input(" Please Enter Natural Number : "))
digit = int(input(" Please Enter Frequency Digit : "))

print frequencydigits(number, digit)


