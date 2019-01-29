import sqlite3

with sqlite3.connect('Employee') as db:
    cursor = db.cursor()
    try:
        cursor.execute('''CREATE TABLE EMP(ID INT, NAME TEXT, DEPT TEXT, SALARY INT)''')
    except Exception as E:
        print "Error: ", E
