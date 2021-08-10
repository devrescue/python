import sqlite3
con = sqlite3.connect('data/sample.db')
cur = con.cursor()

#select rows
for row in cur.execute('SELECT * FROM PlayList'):
    print(row)

cur.execute("DELETE FROM PlayList WHERE id = 1")

#select rows
for row in cur.execute('SELECT * FROM PlayList'):
    print(row)

con.close()