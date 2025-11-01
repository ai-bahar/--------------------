import sqlite3
conn=sqlite3.connect('products.db')
cur=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS لپ تاپ (
    ایدی INTEGER PRIMARY KEY,
    اسم TEXT NOT NULL,
    برند TEXT NOT NULL,
    قیمت INTEGER PRIMARY KEY
    )
""")