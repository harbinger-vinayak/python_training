import re
string = 'This is my string contains number 101 and IP 10.11.12.13'

match = re.search('10.', string)
match1 = re.search('10\.', string)

print match.group()
print match1.group()

match2 = re.search('\d\d', string, re.I)
print match2.group()

match3 = re.search('\w', string, re.I)
print match3.group()

match4 = re.search('ab{0, 5}', string)



# \d for digits
# \w for characters
# \s for spaces

