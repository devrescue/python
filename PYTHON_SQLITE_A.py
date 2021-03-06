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

cur.execute('''CREATE TABLE IF NOT EXISTS Playlist2
              (createdate text, id integer, artist text, songTitle text, albumTitle text, duration text, songprice real)''')

for row in cur.execute('''SELECT name FROM sqlite_schema WHERE type='table' ORDER BY name'''):
    print(row) #shows two tables 
 
# Close connection
con.close()

con = sqlite3.connect('data/sample.db')
cur = con.cursor()

# Drop table
cur.execute('''DROP TABLE IF EXISTS Playlist2''')

for row in cur.execute('''SELECT name FROM sqlite_master WHERE type='table' ORDER BY name'''):
   print(row) #shows one table 

# Close connection
con.close()