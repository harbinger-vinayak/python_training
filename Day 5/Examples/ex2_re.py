import re

with open('file.txt') as infile:
    count = 0
    for line in infile:
        count += 1
        line = line.strip()
        match = re.findall('python', line, flags=re.IGNORECASE)
        if match:
            print '{} contains a word {} for {} times'.format(count, 'python', len(match)) # match.group() replace by 'python'
