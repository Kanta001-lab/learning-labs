# Constants
CURRENCY = "₦"
SEPARATOR = "=" *50


# Orders list
orders = [
    ("1", "2"),  # Egg McMuffin, Medium
    ("2", "1"),  # Sausage Burrito, Small
    ("4", "3"),  # Big Mac, Large
    ("4", "3"),  # Big Mac, Large
    ("3", "2"),  # Mc cafe Iced Coffee, Medium
    ("1", "2"),  # Egg McMuffin, Medium
    ("3", "2")   # Mc cafe Iced Coffee, Medium
]

# Menu items
MC_MENU =  {
    "1": ("Egg McMuffin", 800),
    "2": ("Sausage Burrito", 500),
    "3": ("Mc cafe Iced Coffee", 400),
    "4": ("Big Mac", 1500)
}

# Menu sizes
MC_SIZE = {
    "1": ("Small", 0.7),
    "2": ("Medium", 1.0),
    "3": ("Large", 1.5)
}

# Counters
total_revenue = 0
item_counts = {}  # counts: {"Egg McMuffin": 2, "Big Mac": 1, etc.}
size_counts = {}  # counts: {"Small": 1, "Medium": 2, "Large": 3}
order_totals = [] # Store each order total for average

print("===== MCDONALD'S FACTORY SIMULATOR =====")
print(SEPARATOR)

# Process each order
for order_num, (item_code, size_code) in enumerate(orders, 1):
    # Get item details
    item_name, base_price = MC_MENU[item_code]
    # Get size details
    size_name, multiplier = MC_SIZE[size_code]

    # Calculate order total
    order_total = base_price * multiplier
    order_totals.append(order_total)

    # Update total revenue
    total_revenue += order_total

    # Count items
    # Using get() with default value 0
    item_counts[item_name] = item_counts.get(item_name, 0) + 1

    # Count sizes
    size_counts[size_name] = size_counts.get(size_name, 0) + 1

    # Display order
    print(f"Order #{order_num}:")
    print(f" Item: {item_name}")
    print(f" Size: {size_name}")
    print(f" Price: {order_total:.2f}{CURRENCY}")
    print()

print(SEPARATOR)
print("📊 DAILY STATISTICS")
print(SEPARATOR)

# Total Revenue
print(f" Total Revenue: {total_revenue:.2f}{CURRENCY}")

# Item counts
for item, count in item_counts.items():
    print(f" {item}: {count}")

# Find the most popular item
if item_counts:
    most_popular_item = max(item_counts.items(), key=lambda x: x[1])
    print(f"\n  👑 Most popular Item: {most_popular_item[0]}: {most_popular_item[1]} sold")
    print()

# Size counts
for size, count in size_counts.items():
    print(f" {size}: {count}")

# Find the most popular size
if size_counts:
    most_popular_size = max(size_counts.items(), key=lambda x: x[1])
    print(f"\n  📏 Most popular Size: {most_popular_size[0]}")

# Average order value
if order_totals:
    average_order = sum(order_totals) / len(order_totals)
    print(f"\n Average Order Value: {average_order:.2f}{CURRENCY}")

    # Find min and max order
    min_order = min(order_totals)
    max_order = max(order_totals)
    print(f"  Min order: {min_order:.2f}{CURRENCY}")
    print(f"  Max order: {max_order:.2f}{CURRENCY}")


print(SEPARATOR)
print("✅ Factory Shift Complete!")