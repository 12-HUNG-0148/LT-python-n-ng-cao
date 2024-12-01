import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS uneti (
            id INTEGER PRIMARY KEY,
            "Tên" TEXT,
            "Tuổi" INTEGER
            )
               ''')

cursor.execute('''
            INSERT INTO uneti ("Tên","Tuổi")
            VALUES ("Bùi Huy Hoàng", 19)
            ''')
cursor.execute('''
            INSERT INTO uneti ("Tên","Tuổi")
            VALUES ("Nguyễn Minh Hùng", 19)
            ''')
cursor.execute('''
            INSERT INTO uneti ("Tên","Tuổi")
            VALUES ("Nguyễn Văn A", 19)
            ''')
conn.commit()

cursor.execute("SELECT * from uneti")
rows = cursor.fetchall()

tong = 0
for row in rows:
    tong += 1
print(tong, "là số bản ghi trong csdl")

cursor.close()
conn.close()