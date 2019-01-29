"""
Wap to read csv file which contain following columns emp id, emp name, empsal, empdept
"""

import csv

with open('employee.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print dict(row)


csvfile.close()
