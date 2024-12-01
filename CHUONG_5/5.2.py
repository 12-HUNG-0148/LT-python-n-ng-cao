import sqlite3
conn = sqlite3.connect('mydatabase.db')
conn = sqlite3.connect(':memory:')
