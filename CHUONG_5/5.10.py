import sqlite3
conn = sqlite3.connect('product.db')
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            "Name" TEXT NOT NULL,
            "Price" REAL NOT NULL,
            "Amount" INTEGER NOT NULL
            )
               ''')

cursor.execute('''
            INSERT INTO product ("Name","Price","Amount")
            VALUES ("Banana",20000.0,2),
                   ("Apple",15000.0,1);
            ''')

conn.commit()

# hiển thị danh sách sản phẩm
cursor.execute("SELECT * FROM product")
rows = cursor.fetchall()
for row in rows:
    print(row)

# thêm các sản phẩm vào bảng sản phẩm
cursor.execute('''
            INSERT INTO product ("Name","Price","Amount")
            VALUES ("Mango",25000.0,1)
            ''')
for row in cursor:
    print(row)

# tìm kiếm thông tin sản phẩm theo tên
cursor.execute('''
            SELECT "Name","Price","Amount"
            FROM product;
               ''')
for row in cursor:
    print(row)

# Cập nhật đơn giá, số lượng 1 sản phẩm theo id
cursor.execute('''
            UPDATE product SET "Price" = 23000.0, "Amount" = 5 
            WHERE Id = 2;
               ''')
for row in cursor:
    print(row)

# Xóa 1 sản phẩm theo id cụ thể
cursor.execute('''
            DELETE FROM product
            WHERE Id = 1
               ''')
for row in cursor:
    print(row)
