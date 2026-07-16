import sqlite3

conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# Insert one customer with ? placeholders
cursor.execute('''
    INSERT INTO customers (name, phone, email, total_spent)
    VALUES(?, ?, ?, ?)
''', ('Yasmin', '090980-222-01', 'yasmin342@gail.com', 25000))


# Insert another customer
cursor.execute('''
    INSERT INTO customers (name, phone, email, total_spent)
    VALUES(?, ?, ?, ?)
''', ('Hanna Mutaba', '092980-132-22', 'Mutabahanna@gail.com', 22000))

# Using dictionary
customer_data = {
    'name': 'GoodLuck',
    'phone': '0701-0902-333',
    'email': 'Gods-lucks@gmail.com',
    'total_spent': 100000
}
cursor.execute('''
    INSERT INTO customers (name, phone, email, total_spent)
    VALUES (:name, :phone, :email, :total_spent)
''', customer_data)

# Save changes
conn.commit()
print("✅ Customers added successfully!")


# Check how many customers available
cursor.execute('SELECT COUNT(*) FROM customers')
count = cursor.fetchone()[0]
print(f"Total customers: {count}")