import sqlite3

def get_db():
    conn = None
    try:
        conn = sqlite3.connect('database.db')
    except sqlite3.Error as e:
        print(e)
    return conn

def get_products():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, description, price, vendor_id FROM products"
    cursor.execute(statement)
    return cursor.fetchall()

def insert_product(id, name, description, price, vendor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO products(id, name, description, price, vendor_id) VALUES (?, ?, ?, ?, ?)"

    cursor.execute(statement, [id, name, description, price, vendor_id])
    db.commit()

    return True

def get_product_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, name, description, price, vendor_id FROM products WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()

def update_product(id, name, description, price, vendor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE products SET name = ?, description = ?, price = ?, vendor_id = ?, WHERE id = ?"
    cursor.execute(statement, [name, description, price, vendor_id, id])
    db.commit()

    return True

def delete_product(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM products WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()

    return True

def get_order_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, customer_id, product_id, quantity, total FROM orders WHERE id = ?"
    cursor.execute(statement, [id])

    return cursor.fetchone()

def get_orders_by_vendor(vendor_id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, customer_id, product_id, quantity, total FROM orders WHERE vendor_id = ?"
    cursor.execute(statement, [vendor_id])
    return cursor.fetchall()