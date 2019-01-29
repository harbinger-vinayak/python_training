"""
Find out the avg salary of ITdept
"""


import csv
sal_total = 0
sal_len = 0
with open('employee.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rdict = dict(row)
        sal = rdict['emp_sal']
        sal_total += int(sal)
        sal_len += 1
    avg_total = sal_total / sal_len
    print "Average Salary:", avg_total
csvfile.close()
