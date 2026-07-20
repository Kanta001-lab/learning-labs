import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()


# Show all current customers
cursor.execute('SELECT id, name FROM customers')
for row in cursor.fetchall():
    print(f"ID: {row[0]}, Name: {row[1]}")


# Delete 1: Delete by name
cursor.execute('DELETE FROM customers WHERE name = ?', ('GoodLuck',))

# Delete 2: Delete by ID
cursor.execute('DELETE FROM customers WHERE id = ?', (2,))

print("\nRemaining Customers:")
cursor.execute('SELECT * FROM customers')
all_customers = cursor.fetchall()
for customer in all_customers:
    print(f"{customer[1]}: Phone={customer[2]}")

conn.commit()
conn.close()