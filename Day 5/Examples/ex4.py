"""
wap to accept a password from a user and validate the following
    password should contain atleast 1 character
    password should contain atleast 1 digit
    Password should contain atleast 1 special character
    Password should contain length of password should be greater than 8
"""

import re
"""
inValue = raw_input("Enter a password: ")
match = re.search('\w+\d+[_%#@$&]+......', inValue, re.I)
if match:
    print "Welcome!"
else:
    print "Invalid Password"
"""

inValue = raw_input("Enter a password: ")
match = re.search('[a-zA-Z]', inValue, re.I)
match1 = re.search('[0-9]', inValue, re.I)
match2 = re.search('[_%#@$&]', inValue, re.I)

if match and match1 and match2 and len(inValue) > 8:
    print "Welcome!"
else:
    print "Invalid password"
