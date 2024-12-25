import sqlite3
# ý 1
conn = sqlite3.connect('product.db')
cursor = conn.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS product (
            Id INTEGER PRIMARY KEY,
            "Name" TEXT NOT NULL,
            "Price" REAL NOT NULL,
            "Amount" INTEGER NOT NULL
               )
               '''
)

# ý 2
product_id = int(input("Nhập id sản phẩm: "))
name = input("Nhập sản phẩm bạn muốn thêm: ")
price = float(input("Giá tiền sản phẩm bạn thêm là: "))
amount = int(input("Số lượng sản phẩm bạn muốn thêm là: "))
cursor.execute('INSERT INTO product ("Name","Price","Amount") VALUES (?,?,?)',(name,price,amount))
   
# ý 3
cursor.execute("SELECT Name FROM product")
rows = cursor.fetchall()
for row in rows:
    print(row)

# ý 4
cursor.execute("UPDATE product SET Price=?, Amount=? WHERE Id =?",(price,amount,product_id))

# ý 5
cursor.execute("DELETE FROM product WHERE Id=?", (product_id,))
conn.commit()
conn.close()