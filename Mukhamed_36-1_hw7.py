import sqlite3
conn = sqlite3.connect("hw.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, product_title TEXT NOT NULL, price REAL NOT NULL DEFAULT 0.0, quantity INTEGER NOT NULL DEFAULT 0)")

def add_products():
    products = [
        ("Мыло детское", 50.0, 10),
        ("Шампунь для волос", 120.0, 5),
        ("Зубная паста", 80.0, 8),
        ("Зубная щетка", 40.0, 12),
        ("Гель для душа", 150.0, 6),
        ("Дезодорант", 100.0, 7),
        ("Бальзам для губ", 60.0, 9),
        ("Крем для рук", 90.0, 4),
        ("Крем для лица", 200.0, 3),
        ("Туалетная бумага", 30.0, 15),
        ("Салфетки влажные", 25.0, 20),
        ("Маска для лица", 70.0, 10),
        ("Скраб для тела", 180.0, 5),
        ("Лосьон для тела", 190.0, 4),
        ("Пена для бритья", 110.0, 6)
    ]
    cur.executemany("INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)", products)
    conn.commit()


def update_quantity(id, new_quantity):
    cur.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, id))
    conn.commit()

def update_price(id, new_price):
    cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, id))
    conn.commit()

def delete_product(id):
    cur.execute("DELETE FROM products WHERE id = ?", (id,))
    conn.commit()

def select_all_products():
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    print("id | product_title | price | quantity")
    print("-" * 40)
    for product in products:
        print(product[0], "|", product[1], "|", product[2], "|", product[3])


def select_cheap_and_many_products():
    cur.execute("SELECT * FROM products WHERE price < 100 AND quantity > 5")
    products = cur.fetchall()
    print("id | product_title | price | quantity")
    print("-" * 40)
    for product in products:
        print(product[0], "|", product[1], "|", product[2], "|", product[3])


def search_products_by_title(keyword):
    cur.execute("SELECT * FROM products WHERE product_title LIKE ?", ("%" + keyword + "%",))
    products = cur.fetchall()
    print("id | product_title | price | quantity")
    print("-" * 40)
    for product in products:
        print(product[0], "|", product[1], "|", product[2], "|", product[3])


add_products()
update_quantity(1, 20)
update_price(2, 150.0)
delete_product(15)
select_all_products()