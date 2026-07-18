import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()



# Get all customers
cursor.execute('SELECT * FROM customers')
all_customers = cursor.fetchall()

for customer in all_customers:
    print(f"ID: {customer[0]}, Name: {customer[1]}, Phone: {customer[2]}")



# Search for a specific customer
print("\nSearch for Timothy")
search_name = '%Timothy%'
cursor.execute('SELECT * FROM customers WHERE name LIKE ?', (search_name,))
results = cursor.fetchall()
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Spent: ₦{row[4]}")



# Get customers who spent over 50k
print("\nBig Spenders")
cursor.execute('SELECT * FROM customers WHERE total_spent > 50000')
big_spenders = cursor.fetchall()
for customer in big_spenders:
    print(f"ID: {customer[0]}, Name: {customer[1]}, Spent: {customer[4]:,.2f}")



# Get just one customer (first result)
print("\n First Customer:")
cursor.execute('SELECT * FROM customers LIMIT 1')
first_customer = cursor.fetchone()
if first_customer:
    print(f"First Customer: {first_customer[1]}")


conn.close()

# Query Methods:
# - fetchall(): Gets All results as a list
# - fetchone(): Gets just ONE result
# - fetchmany(n): Gets a specific number of results