import sqlite3
DB_PATH = "laptops.db"
conn=sqlite3.connect('laptops.db')
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS "لپ تاپ ها" (
    ایدی INTEGER PRIMARY KEY AUTOINCREMENT,
    نام TEXT ,
    برند TEXT ,
    قیمت INTEGER ,
    سی_پی_یو TEXT ,
    رم INTEGER ,
    حافظه INTEGER ,
    جی_پی_یو TEXT ,
    صفحه_نمایش TEXT ,
    باتری TEXT ,
    وزن REAL
)
""")

laptops = [
    ["Vivobook Go 15 A1504", "ASUS", 42000000, "i3-N305", 4, 256, "UHD", "15.6\" FHD IPS", "42Wh", 1.69],
    ["IdeaPad Slim 3 Gen 9", "Lenovo", 37000000, "i3-1305U", 8, 256, "UHD", "15.6\" TN FHD", "45Wh", 1.65],
    ["HP 15s-fq5000", "HP", 24000000, "i3-1215U", 8, 512, "UHD", "15.6\" FHD", "41Wh", 1.69],
    ["MacBook Air M1 (2025)", "Apple", 120000000, "Apple M1", 8, 256, "integrated", "13.3\" Retina", "49.9Wh", 1.29],
    ["Chromebook CX1500", "ASUS", 16800000, "Celeron N4500", 4, 128, "UHD", "15.6\" FHD Matte", "38Wh", 1.8],
    ["Chromebook Duet 5", "Lenovo", 59400000, "Snapdragon 7c Gen2", 8, 128, "Adreno 618", "13.3\" OLED Touch", "42Wh", 0.7],
    ["Zenbook 14 OLED A1405", "ASUS", 70000000, "Ryzen 5 8640HS", 16, 512, "iGPU", "14\" OLED 2.8K", "75Wh", 1.39],
    ["Yoga Slim 7i Gen 9", "Lenovo", 89900000, "i5-13500H", 16, 512, "iGPU", "14\" OLED", "65Wh", 1.39],
    ["Pavilion Plus 14 2025", "HP", 73000000, "i5-1340P", 16, 512, "Iris Xe", "14\" OLED 2.8K", "51Wh", 1.44],
    ["MacBook Air M2 (2025)", "Apple", 125000000, "Apple M2", 16, 512, "integrated", "13.6\" Retina", "52.6Wh", 1.24],
    ["Vivobook Pro 15 OLED K6502", "ASUS", 63000000, "i5-13500H", 16, 512, "RTX 3050", "15.6\" OLED 2.8K", "70Wh", 1.8],
    ["Legion Slim 5 Gen 10", "Lenovo", 105000000, "Ryzen 7 7840HS", 16, 1000, "RTX 4060", "15.1\" OLED WQXGA", "80Wh", 1.9],
    ["ROG Zephyrus G16 2025", "ASUS", 400000000, "Ultra 9 285H", 32, 2000, "RTX 5080", "16\" OLED 2.5K", "90Wh", 1.95],
    ["Legion Pro 7i Gen 10", "Lenovo", 410000000, "Ultra 9 275HX", 64, 2000, "RTX 5080ac", "16\" OLED WQXGA", "99.9Wh", 2.57],
    ["Omen Transcend 16 2025", "HP", 305000000, "i9-14900HX", 32, 2000, "RTX 4070", "16.1\" FHD IPS", "97Wh", 2.17],
    ["MacBook Pro M3 Max 16\"", "Apple", 441000000, "M3 Max", 48, 1000, "integrated", "16.2\" Retina XDR", "100Wh", 2.15],
    ["ProArt Studiobook 16 OLED", "ASUS", 300000000, "i9-13980HX", 32, 2000, "RTX 4070", "16\" OLED 3.2K", "90Wh", 2.4],
    ["ThinkPad P1 Gen 7", "Lenovo", 536000000, "Ultra 7 155H", 64, 2000, "RTX 4060", "16\" IPS WQXGA", "90Wh", 1.82],
    ["ROG Strix Scar 16 2025", "ASUS", 530000000, "Ultra 9 275HX", 32, 2000, "RTX 5090", "16\" Mini LED HDR", "90Wh", 2.85],
    ["MacBook Pro 14 M5 (2025)", "Apple", 278000000, "M5", 16, 512, "integrated", "14.2\" Retina XDR", "70Wh", 1.55]
]

for laptop in laptops:
    cursor.execute("""
    INSERT INTO "لپ تاپ ها" (نام, برند, قیمت, سی_پی_یو, رم, حافظه, جی_پی_یو, صفحه_نمایش, باتری, وزن)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, laptop)
def همه_نام_ها():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT نام FROM "لپ تاپ ها"')
    names = [r[0] for r in cur.fetchall()]
    conn.close()
    return names
conn.commit()
conn.close()


