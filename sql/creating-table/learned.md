# Understanding the Code:

1. `sqlite3.connect('restaurant.db)`: Creates a connection to the database file
2. `cursor = conn.cursor()`: Creates a cursor to execute SQL commands
3. `CREATE TABLE IF NOT EXISTS`: Creates a table only if it doesn't exist
4. `conn.commit()`: Saves all changes to the database
5. `conn.close()`: Closes the connection (always implement this.)

## Data Types in SQlite

- Integer: Whole numbers
- TEXT: Text/Strings
- REAL: Decimal numbers
- Null: Empty values

# Common Mistakes

## Forgetting to commit()

```python
# Wrong 
cursor.execute('INSERT INTO customers ...')
# changes not saved!


# Correct
cursor.execute('INSERT INTO customers ...')
conn.commit() # Saves the changes!
```

## Not closing connections

```python
# Wrong
conn = sqlite3.connect('database.db')
# Work with database
# Never close connection - Bad practice

# Correct
conn = sqlite3.connect('database.db')
# Work with database
conn.close()
```
