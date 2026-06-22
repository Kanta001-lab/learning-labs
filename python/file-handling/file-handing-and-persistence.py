"""
=======================================================================
01: READING AND WRITING TEXT FILES
=======================================================================
"""

# =======================================================================
# Opening a fie - the safe way
# =======================================================================

# The "with" statement automatically closes the file
with open("test.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("Second line.\n")

"""
'w' = write mode (creates and overwrites)
'r' = read mode (default)
'a' = append mode (adds to end)
"""

# =======================================================================
# Reading a file
# =======================================================================
with open("test.txt", "r") as f:
    content = f.read()    # whole file as one string
    print(content)

with open("test.txt", "r") as f:
    lines = f.readlines()   # list of lines (including \n)
    for line in lines:
        print(line.strip())


# =======================================================================
# Appending to a file
# =======================================================================
with open("test.txt", "a") as f:
    f.write("third line.\n")


"""
=======================================================================
02: STRUCTURED DATA WITH JSON
=======================================================================
"""

# =======================================================================
# Writing a dictionary to JSON
# =======================================================================
import json

data = {
    "name": "Python Bistro",
    "orders": [
        {"id": 1, "total": 3500},
        {"id": 2, "total": 8000}
    ]
}

with open("restaurant_data.json", "w") as f:
    json.dump(data, f, indent=4)   # indent makes it readable


# =======================================================================
# Reading JSON
# =======================================================================
with open("restaurant_data.json", "r") as f:
    loaded_data = json.load(f)
    print(loaded_data["name"])
    print(loaded_data["orders"][0]["total"])



"""
=======================================================================
03: TABULAR DATA WITH CSV
=======================================================================
"""

# =======================================================================
# Writing a list of orders to CSV
# =======================================================================

import csv

orders = [
    ["Order ID", "Customer", "Total"],
    [1, "Femi", 3800],
    [2, "Ali", 5000]
]

with open("orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(orders)


# =======================================================================
# Reading CSV
# =======================================================================
with open("orders.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# If you have dictionaries, use csv.DictWriter / DictReader
orders_dicts = [
    {"id": 1, "customer": "Femi Gold", "total": 3800},
    {"id": 2, "customer": "Ali Mohammed", "total": 5000},
]

with open("orders_dict.csv", "w", newline="") as f:
    fieldnames = ["id", "customer", "total"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(orders_dicts)

with open("orders_dict.csv", "r", newline="") as f:
    fieldnames = ["id", "customer", "total"]
    reader = csv.DictReader(f, fieldnames=fieldnames)
    for read in reader:
        print(read)
