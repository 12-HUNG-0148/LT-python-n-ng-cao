import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS dhkl (
            id INTEGER PRIMARY KEY,
            "Tên" TEXT,
            "Tuổi" INTEGER
            )
               ''')

cursor.execute('''
            INSERT INTO dhkl ("Tên","Tuổi")
            VALUES ("Bùi Huy Hoàng", 19)
            ''')

conn.commit()

cursor.execute("SELECT * from dhkl")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()