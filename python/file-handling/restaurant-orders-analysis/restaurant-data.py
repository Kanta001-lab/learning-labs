import csv

# restaurant orders file
restaurant_orders = [
     ["order_id", "customer_name", "item", "quantity", "price", "order_date", "status"],
    [1001, "Haruna Umar", "Margherita Pizza", 2, 8000, "2024-01-15", "delivered"],
    [1002, "Aisha Sani", "Caesar Salad", 1, 4500, "2024-01-15", "delivered"],
    [1003, "Muhammad Gebe", "Spaghetti Carbonara", 1, 6500, "2024-01-16", "preparing"],
    [1004, "Sarah Ade", "Garlic Bread", 3, 2500, "2024-01-16", "delivered"],
    [1005, "James Davis", "Tiramisu", 2, 4500, "2024-01-17", "cancelled"],
    [1006, "Hassan Ilyasu", "Fettuccine Alfredo", 1, 11000, "2024-01-17", "delivered"],
    [1007, "Isreal Ouinloye", "Pepperoni Pizza", 1, 8000, "2024-01-18", "preparing"],
    [1008, "Ibrahim Yusuf", "Bruschetta", 2, 6500, "2024-01-18", "delivered"],
    [1009, "David Jafar", "Chicken Parmesan", 1, 10000, "2024-01-19", "delivered"]
]

with open("restaurant_orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(restaurant_orders)

print("✅ File created: restaurant_orders.csv")