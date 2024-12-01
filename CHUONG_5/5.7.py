import sqlite3
conn = sqlite3.connect('mydatabase.db')
conn.execute("UPDATE uneti SET 'Tên' = 'Nguyễn Minh Hùng' where id = 1")
conn.commit()

cursor = conn.execute("SELECT * FROM uneti")
for row in cursor:
    print(row)
conn.close()