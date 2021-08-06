import sqlite3
con = sqlite3.connect('data/sample.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS Playlist
              (createdate text, 
               id integer, 
               artist text, 
               songTitle text, 
               albumTitle text, 
               duration text, 
               songprice real)''')

# Insert a row of data
cur.execute("INSERT INTO PlayList VALUES ('2022-01-31',1,'Kanye West','Fade','Life of Pablo','3:13',2.99)")
cur.execute("INSERT INTO PlayList VALUES ('2022-01-31',2,'Kanye West','Ultralight Beam','Life of Pablo','5:20',3.99)")
cur.execute("INSERT INTO PlayList VALUES ('2022-01-31',3,'Kanye West','Famous','Life of Pablo','3:16',1.99)")

# Save (commit) the changes
con.commit()

#select rows
for row in cur.execute('SELECT * FROM PlayList'):
    print(row)

#select rows
for row in cur.execute('SELECT * FROM PlayList WHERE songprice > 3'):
    print(row)
    
#select rows
for row in cur.execute("SELECT * FROM PlayList WHERE songTitle LIKE '%Fa%'"):
    print(row)

con.close()