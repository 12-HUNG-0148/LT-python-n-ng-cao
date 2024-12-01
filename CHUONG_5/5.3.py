import sqlite3
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute(
    ("""
    CREATE TABLE SV (
    Ten TEXT,
    Tuoi INTEGER)
    """)
)
conn.close()
