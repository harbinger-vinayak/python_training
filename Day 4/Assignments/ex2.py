"""
Assignment of Day 4 and Day 5
Read CSV from quandl.com and insert to database
"""
import requests
import sys
import json
import xlwt
import csv
import sqlite3

sList = []
with open('symbols.csv') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
        symbol = row[0]
        authkey = 'CZaTnx9DAjD7nTBpVJhV'
        url = 'https://www.quandl.com/api/v3/datasets/AMFI/{}.json?api_key={}'.format(symbol, authkey)

        response = requests.get(url)

        if response.status_code != 200:
            sys.exit(1)

        dList = []
        content = json.loads(response.content)
        share_name = content['dataset']['name']
        dList.append(share_name)
        dList.append(symbol)
        for data in (content['dataset']['data'])[:2]:
            dList.append(data[0])
            dList.append(data[1])

        pl = dList[3] - dList[5]
        dList.append(round(pl, 4))
        sList.append(dList)
csvfile.close()

excel_file = xlwt.Workbook()
sheet = excel_file.add_sheet('demo')
style = xlwt.XFStyle()
# font
font = xlwt.Font()
font.bold = True
style.font = font
# borders
borders = xlwt.Borders()
borders.bottom = xlwt.Borders.DASHED
style.borders = borders
# colour
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN

sheet.write(0, 0, "Share Name", style=style)
sheet.write(0, 1, "Symbol", style=style)
sheet.write(0, 2, "Last Date", style=style)
sheet.write(0, 3, "Last Value", style=style)
sheet.write(0, 4, "Last Date - 1", style=style)
sheet.write(0, 5, "Last Value - 1", style=style)
sheet.write(0, 6, "Profit/Loss", style=style)

for row_index, row_contents in enumerate(sList):
    for column_index, cell_value in enumerate(row_contents):
        if column_index == 6 and cell_value < 0:
            pattern.pattern_fore_colour = xlwt.Style.colour_map['red']
            style.pattern = pattern
            sheet.write(row_index+1, column_index, cell_value, style=style)
        elif column_index == 6 and cell_value > 0:
            pattern.pattern_fore_colour = xlwt.Style.colour_map['green']
            style.pattern = pattern
            sheet.write(row_index + 1, column_index, cell_value, style=style)
        else:
            sheet.write(row_index + 1, column_index, cell_value)
excel_file.save("test.xls")

# Insert into DB
with sqlite3.connect('dataDB') as db:
    cursor = db.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS INSIGHTS(SHARE_NAME TEXT, SYMBOL TEXT, LAST_DATE TEXT, LAST_VALUE FLOAT,\
        LAST_DATE_1 TEXT, LAST_VALUE_1 FLOAT, PROFIT_LOSS FLOAT)''')

        if sList:
            cursor.executemany('''INSERT INTO INSIGHTS VALUES(?, ?, ?, ?, ?, ?, ?)''', sList)

        sql = '''SELECT * FROM INSIGHTS'''
        cursor.execute(sql)
    except Exception as E:
        print "Error: ", E
    else:
        db.commit()
        result = cursor.fetchall()
        print "Total number of rows in table is", len(result)
        row_number = 1
        for row in result:
            print "Row No.", row_number, ": ", row
            row_number += 1
