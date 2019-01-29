import sqlite3

id = input('Enter a ID: ')
name = raw_input('Enter a name: ')
dept = raw_input('Enter a department: ')
salary = input("Enter a salary: ")

with sqlite3.connect('Employee') as db:
    cursor = db.cursor()
    try:
        # sql = '''INSERT INTO EMP VALUES({}, '{}', '{}', {})'''.format(id, name, dept, salary)
        # cursor.execute(sql)
        cursor.execute('''INSERT INTO EMP VALUES(?, ?, ?, ?)''', (id, name, dept, salary))
        # for multiple insert use following
        # cursor.executemany('''Query''', [(), (), {}, {}])
    except Exception as E:
        print "Error: ", E
    else:
        db.commit()
