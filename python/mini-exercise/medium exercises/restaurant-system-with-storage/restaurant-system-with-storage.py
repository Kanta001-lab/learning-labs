import json
import csv
from datetime import datetime

SEPARATOR = "=" * 50
CURRENCY = "₦"

class MenuItem:
    def __init__(self, name, price, category, prep_time):
        self.name = name
        self.price = price
        self.category = category
        self.prep_time = prep_time
        self.orders_count = 0

class Orders:
    def __init__(self, order_id, customer_name, table_number):
        self.order_id = order_id
        self.customer_name = customer_name
        self.table_number = table_number
        self.items = []
        self.order_time = datetime.now()
        self.status = "pending"


    def add_item(self, menu_item, quantity=1):
        self.items.append((menu_item, quantity))
        menu_item.orders_count += quantity

    def calculate_total(self):
        return sum(item.price * qty for item, qty in self.items)



class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []
        self.next_order_id = 1

        if not self.load_menu("menu.json"):
            self._setup_default_menu()

    def _setup_default_menu(self):
        """Default menu if no file exist"""
        default_items = [
            ("Jollof Rice",  8500, "main", 12),
            ("Egusi & Swallow", 8500, "main", 15),
            ("Asun", 5500, "appetizer", 7),
            ("Pepper Soup", 5500, "appetizer", 5),
            ("Soft Drink", 1500, "drink", 2),
        ]
        for name, price, category, prep_time in default_items:
            self.menu.append(MenuItem(name, price, category, prep_time))


    def save_menu(self, filename="menu.json"):
        """Save menu to JSON file"""
        menu_data = []
        for item in self.menu:
            menu_data.append({
                "name": item.name,
                "price": item.price,
                "category": item.category,
                "prep_time": item.prep_time,
                "orders_count": item.orders_count
            })

        with open(filename, "w") as f:
            json.dump(menu_data, f, indent=4)
        print(f"✅ Menu saved to {filename}")

    def load_menu(self, filename="menu.json"):
        """Load menu file"""
        try:
            with open(filename, "r") as f:
                menu_data = json.load(f)


            self.menu = []
            for item_data in menu_data:
                item = MenuItem(
                    item_data["name"],
                    item_data["price"],
                    item_data["category"],
                    item_data["prep_time"],
                )
                item.orders_count = item_data.get("orders_count", 0)
                self.menu.append(item)
            print(f"✅ Menu loaded from {filename} ({len(self.menu)} items)")
            return True
        except FileNotFoundError:
            print(f"⚠️ No menu file found. Using default menu")
            return False

    def create_order(self, customer_name, table_number):
        """Create new order"""
        order = Orders(self.next_order_id, customer_name, table_number)
        self.orders.append(order)
        self.next_order_id += 1
        print(f"\n Order #{order.order_id} created for {customer_name}")
        print()
        return order

    def save_daily_report(self, filename=None):
        """save daily report to text file"""
        if filename is None:
            filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

            with open(filename, "w") as f:
                # Header
                f.write(SEPARATOR + "\n")
                f.write(f"{self.name} - DAILY REPORT\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(SEPARATOR + "\n\n")

                # Statistics
                total_orders = len(self.orders)
                total_revenue = sum(order.calculate_total() for order in self.orders)

                f.write(f"Total Orders: {total_orders}\n")
                f.write(f"Total Revenue: {total_revenue:.2f}\n")

                if total_orders > 0:
                    avg_order = total_revenue / total_orders
                    f.write(f"Average Order: {avg_order:.2f}\n\n")

                # Order details
                f.write("\n ORDER DETAILS:\n")
                f.write(SEPARATOR + "\n")
                for order in self.orders:
                    f.write(f"Order #{order.order_id} - Table {order.table_number}\n")
                    f.write(f"  Customer: {order.customer_name}\n")
                    f.write(f"  Time: {order.order_time.strftime('%H:%M:%S')}\n")
                    f.write(f"  Total: {order.calculate_total():.2f}\n")
                    f.write(f"  Status: {order.status}\n")
                    f.write("\n")

                print(f"✅ Daily report saved to {filename}")

    def append_order_to_csv(self, filename="order_history.csv"):
        """Append new orders to CSV file"""
        # Check if file exists to write header
        file_exists = False
        try:
            with open(filename, 'r'):
                file_exists = True
        except FileNotFoundError:
            pass

        # Open in append mode
        with open(filename, "a", newline="") as f:
            writer = csv.writer(f)

            # Header if file is new
            if not file_exists:
                writer.writerow(["Order ID", "Date", "Time", "Customer",
                                 "Table", "Total", "Status", "Items"])

            # All orders Appended
            for order in self.orders:
                items_summary = "; ".join([f"{qty}x {item.name}"
                                           for item, qty in order.items])
                writer.writerow([
                    order.order_id,
                    order.order_time.strftime('%Y-%m-%d'),
                    order.order_time.strftime('%H:%M:%S'),
                    order.customer_name,
                    order.table_number,
                    f"{order.calculate_total():.2f}",
                    order.status,
                    items_summary
                ])

        print(f"✅ Orders appended to {filename}")


if __name__ == '__main__':
    print(SEPARATOR)
    print("TESTING RESTAURANT WITH FILE STORAGE")
    print(SEPARATOR)

    # restaurant (will try to load menu)
    restaurant = Restaurant("Python Bistro")

    # Add some orders
    order1 = restaurant.create_order("Ali Mohammad", 5)
    # Add items using menu index
    if len(restaurant.menu) >= 3:
        order1.add_item(restaurant.menu[0], 2)  # 2 Jollof Rice
        order1.add_item(restaurant.menu[4], 3)  # 3 Soft Drinks
        order1.status = "completed"

    order2 = restaurant.create_order("Juliet Nwosu", 3)
    if len(restaurant.menu) >= 3:
        order2.add_item(restaurant.menu[1], 1)  # Egusi & Swallow
        order2.add_item(restaurant.menu[3], 2)  # Pepper Soup
        order2.status = "completed"

    order3 = restaurant.create_order("Clinton Price", 2)
    if len(restaurant.menu) >= 3:
        order3.add_item(restaurant.menu[0], 1)  # Jollof Rice
        order3.add_item(restaurant.menu[2], 2)  # Asun
        order3.add_item(restaurant.menu[4], 1)  # Soft Drink
        order3.status = "completed"

    # Save menu
    restaurant.save_menu()

    # Save daily report
    restaurant.save_daily_report()

    # Append to CSV
    restaurant.append_order_to_csv()

    print("\n✅ All data saved successfully!")