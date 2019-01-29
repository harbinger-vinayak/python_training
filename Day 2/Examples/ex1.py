'''
1) Except a number from a user and print 10 odd numbers after that number
2) Print first 10 odd numbers
3) Print the sum of first 10 even numbers
'''

number = raw_input("Enter a number: ")
num = range(1, 10, 2)
while num >= 10:
    print num
    break
else:
    print "While completed"



