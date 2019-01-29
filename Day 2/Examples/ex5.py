"""
convert fibonacci, factorial, prime number programs into udf functions
"""

def fibonacci(number):
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

def prime(number):
    var = [i for i in range(2, number) if all(i % j for j in range(2, number))]
    print var

user_value = raw_input("Enter a user input: ")
print "Fibonacci Series: ", fibonacci(number = int(user_value))
print "Prime Series: ", prime(number = int(user_value))