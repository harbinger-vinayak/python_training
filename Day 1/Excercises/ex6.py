x = "There are %d types of people." % 10  # This statement is used integer format character
binary = "binary"  # Assign variable
do_not = "don't"  # Assign variable
y = "Those who know %s and those who %s." % (binary, do_not)  # This statement is used string format character

print x  # This statement is print variable x statement
print y  # This statement is print variable y statement

print "I said: %r." % x  # This statement is used string format character using repr() function
print "I also said: '%s'." % y  # This statement is used string format character using str() function

hilarious = False  # This is boolean variable
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious  # This statement is used string format character using repr() function

w = "This is the left side of..."
e = "a string with a right side."

print w + e  # This statement is used concatenation operator (+) for concat two string

"""
str() is used for creating output for end user 
repr() is mainly used for debugging and development.
"""