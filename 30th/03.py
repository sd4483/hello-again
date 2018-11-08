import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='dab1' user='postgres' password='amber' host='localhost' port='5433'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='dab1' user='postgres' password='amber' host='localhost' port='5433'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)" ,(item, quantity, price))
    conn.commit()
    conn.close()

def view_db():
    conn = psycopg2.connect("dbname='dab1' user='postgres' password='amber' host='localhost' port='5433'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete_db(item):
    conn = psycopg2.connect("dbname='dab1' user='postgres' password='amber' host='localhost' port='5433'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()

def update_db(quantity, price, item):
    conn = psycopg2.connect("dbname='dab1' user='postgres' password='amber' host='localhost' port='5433'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s", (quantity,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Apple", 10, 15)
#insert("Grape", 20, 7.0)
#update_db(20,7.0, 'Grapes')
#delete_db('Apple')
#update_db(20, 15.0, 'Orange')
print(view_db())