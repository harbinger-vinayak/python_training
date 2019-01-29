'''
1) write a program to find out a fibonacci series
2) write a program to find factorial of a number
3) write a program to find out prime numbers between 2 to 100
'''

number = raw_input("Enter a number: ")
variable = 0
variable2 = 1
count = 0
while count < int(number):
    print variable
    nth = variable + variable2
    variable = variable2
    variable2 = nth
    count += 1
else:
    print "End while"

