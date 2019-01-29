import sqlite3

with sqlite3.connect('Employee') as db:
    cursor = db.cursor()
    try:
        sql = '''SELECT * FROM EMP'''
        cursor.execute(sql)
    except Exception as E:
        print "Error: ", E
    else:
        for row in cursor.fetchall():
        # for row in cursor.fetchone():
            print row
