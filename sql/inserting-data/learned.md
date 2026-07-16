# Why use? Placeholders?

- Security: Prevents SQL injection attacks
- Safty: Automatically handles quotes and special characters
- Makes code cleaner

# Common Mistakes

### Using f-string in SQL (**Dangerous**)
*it's adviced to use either the quetion mark or named named stlye*

### Using the Question mark placeholder
```python
# Bad practice - SQL injection risk!
name = "Timothy"
cursor.execute(f"SELECT * FROM customers WHERE name = '{name}'")

# Better: use placeholers
cursor.execute("SELECT * FROM customers WHERE name = ?", (name,))
```