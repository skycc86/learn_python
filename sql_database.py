import sqlite3

def create_table(db='lite.db'):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
  conn.commit()
  conn.close()
  
def insert(item, quantity, price, db='lite.db'):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price))
  conn.commit()
  conn.close()
  
  
  
def delete(item, db='lite.db'):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute("DELETE FROM store WHERE item=?", (item,))
  conn.commit()
  conn.close()
  
def update(item, quantity, price, db='lite.db'):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity,price,item))
  conn.commit()
  conn.close()



def view(db='lite.db'):
  conn = sqlite3.connect(db)
  cur = conn.cursor()
  cur.execute("SELECT * FROM store")
  rows = cur.fetchall()
  conn.close()
  return rows
  
create_table()
insert('Water Glass',5,10.5)
insert('Coffee Cup',2,10.5)
delete('Cofffee Cup')
update('Coffee Cup', 100, 50)
print(view())

