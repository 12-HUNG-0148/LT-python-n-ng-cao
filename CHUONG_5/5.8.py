import sqlite3
conn = sqlite3.connect('mydatabase.db')
conn.execute("DELETE FROM uneti where id=3")
conn.commit()

cursor = conn.execute("SELECT * FROM uneti")
for row in cursor:
    print(row)
conn.close()