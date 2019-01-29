"""
wap to read weblog and identify the occurances of IP addresses hit in that particular date
"""

"""
\d+\.\d+\.\d+\.\d+ It check ip without group for search
"""

import re

"""
string = "This is is an IP 10.02.3.19"
# pattern = '(\d+)\.(\d+)\.(\d+)\.\d+'
pattern = '\d+\.\d+\.\d+\.\d+'

match = re.findall(pattern, string)
# match = re.search(pattern, string)
# print match.groups()
# print match.group(1)
# print match.group()
print match
"""

with open('file.txt') as infile:
    count = 0
    for line in infile:
        count += 1
        line = line.strip()
        match = re.findall('python', line, flags=re.IGNORECASE)
        if match:
            print '{} contains a word {} for {} times'.format(count, 'python', len(match)) # match.group() replace by 'python'

pattern = '\d+\.\d+\.\d+\.\d+'
match = re.findall(pattern, string)
