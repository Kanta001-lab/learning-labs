import sqlite3

# Connect to a database (creates file if it does not exista)
conn = sqlite3.connect("restaurant.db")
cursor = conn.cursor()

# Create first table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    total_spent REAL DEFAULT 0
    )
''')

# Save changes
conn.commit()


# Check if table was created
cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall
print(f"Tables in database: {tables}")

# Close connection
conn.close