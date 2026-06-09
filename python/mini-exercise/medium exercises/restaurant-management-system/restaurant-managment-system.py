from collections import defaultdict, Counter
from datetime import datetime
import random


# CONSTANTS
CURRENCY = "₦"
SEPARATOR = "=" * 50


class RestaurantManager:
    """
    Manages restaurant operations including orders, customers, and statistics.

    Attributes:
        orders: (list)
            A chronological list of all the orders.

        customers: defaultdict(list)
            Maps customer names to their order history.

        hourly_orders: defaultdict(list)
            Chronologically maps all orders by the hour.

        popular_item: (Counter)
            Tracks total quantity for each item for popularity tracking.

        total_revenue: (float)
            Total revenue for each order per unit.

        open_time: (None)

        close_time: (None)
            
    Example:
        >>> restaurant = RestaurantManager()
        >>> restaurant.open_restaurant()
        >>> restaurant.simulate_busy_hour("2")  # Lunch
        >>> restaurant.simulate_busy_hour("8")  # Dinner
        >>> restaurant.close_restaurant()

    Notes:
        - Timestamps are auto-generated in 24-hour format (HH:MM)
        - Customer names are case-sensitive
        - Item counts use Counter.most_common() for ranking
    """

    def __init__(self, name="My Restaurant"):
        self.name = name

        # List of all orders
        self.orders = []

        # Customer order history
        self.customers = defaultdict(list)

        # hour → list of orders
        self.hourly_orders = defaultdict(list)
        self.popular_items = Counter()
        self.total_revenue = 0.0

        # Time restaurant opens
        self.open_time = None

        # Time restaurant closes
        self.close_time = None

        print(f"\n🏢 {self.name} Management System Initialized!")
        print(SEPARATOR)

    def open_restaurant(self):
        """Open time for business"""
        self.open_time = datetime.now()
        print(f"\n🔓 Restaurant OPENED at {self.open_time.strftime('%H:%M')}")
        print("Ready to take orders!")

    def close_restaurant(self):
        """Close and generate final report"""
        self.close_time = datetime.now()
        print(f"\n🔒 Restaurant CLOSED at {self.close_time.strftime('%H:%M')}")
        self.generate_daily_report()

    def take_order(self, customer_name, items):
        """Process a new order"""
        print(f"\n📝 New Order - Customer: {customer_name}")

        order_total = sum(item["price"] * item["qty"] for item in items)

        order = {
            "id": len(self.orders) + 1,
            "customer": customer_name,
            "items": items,
            "total": order_total,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "hour": datetime.now().strftime("%H")
        }

        # Store the order
        self.orders.append(order)
        self.customers[customer_name].append(order)
        self.hourly_orders[order["hour"]].append(order)

        # Update revenue and popular items
        self.total_revenue += order_total
        for item in items:
            self.popular_items[item["name"]] += item["qty"]

        # order details
        print(f" Order #{order['id']} at {order['timestamp']}")
        for item in items:
            print(f"  {item['qty']}x {item['name']} @ {CURRENCY}{item['price']:.2f}")
        print(f" 💰 Total: {CURRENCY}{order_total:.2f}")

        return order

    def get_customer_history(self, customer_name):
        """Get all orders for a customer"""
        print(f"\n📋 CUSTOMER HISTORY: {customer_name}")
        print(SEPARATOR)

        orders = self.customers.get(customer_name, [])
        if not orders:
            print(f"  No order history for {customer_name}")
            return []

        total_spent = sum(o["total"] for o in orders)
        print(f"  Total Orders: {len(orders)}")
        print(f"  Total Spent: {CURRENCY}{total_spent:.2f}")
        print(f"  Average Order: {CURRENCY}{total_spent / len(orders):.2f}")

        print(f"\n RECENT ORDERS:")
        for order in orders[-3:]:
            item_summary = ", ".join([f"{i['qty']}x {i['name']}" for i in order["items"]])
            print(f"  {order['timestamp']} - {item_summary} - {CURRENCY}{order['total']:.2f}")

        return orders

    def get_hourly_summary(self):
        """Analyze orders by hour"""
        print(f"\n⏰ HOURLY BREAKDOWN")
        print(SEPARATOR)

        if not self.hourly_orders:
            print(" No orders yet today")
            return {}

        # Create bar chart data
        max_orders = max(len(order) for order in self.hourly_orders.values())

        for hour in self.hourly_orders.keys():
            count = len(self.hourly_orders[hour])
            revenue = sum(o["total"] for o in self.hourly_orders[hour])

            # create bar chart
            bar_length = int((count / max_orders) * 20) if max_orders > 0 else 0
            bar = "█" * bar_length

            print(f"  {hour}:00 | {bar} {count} orders | {CURRENCY}{revenue:.2f}")

        # Find peak hour
        peak_hour = max(self.hourly_orders.items(), key=lambda x: len(x[1]))
        print(f" 📈 Peak Hour: {peak_hour[0]}:00 with {len(peak_hour[1])} orders")

        return dict(self.hourly_orders)

    def get_popular_item(self, top_n=5):
        """Get most popular items"""
        print(f"\n🥇 TOP {top_n} ITEMS")
        print(SEPARATOR)

        if not self.popular_items:
            print("No sales yet today")
            return []

        for item, count in self.popular_items.most_common(top_n):
            # Calculate revenue for this item
            revenue = 0
            for order in self.orders:
                for ordered_items in order["items"]:
                    if ordered_items["name"] == item:
                        revenue += ordered_items["price"] * ordered_items["qty"]

            print(f" {count:3d}x {item:15} | {CURRENCY}{revenue:.2f}")

        return self.popular_items.most_common(top_n)

    def generate_daily_report(self):
        """Generate end-of-day report"""
        print("\n" + SEPARATOR)
        print(f"📋 DAILY REPORT - {self.name}")
        print(SEPARATOR)

        # Basic stats
        total_orders = len(self.orders)
        print(f"\n📊 SUMMARY")
        print(f"  Total Orders: {total_orders}")
        print(f"  Total Revenue: {CURRENCY}{self.total_revenue:.2f}")

        if total_orders > 0:
            avg_order = self.total_revenue / total_orders
            print(f"  Average Order: {CURRENCY}{avg_order:.2f}")
            print(f"  Unique Customers: {len(self.customers)}")

        # Popular items
        self.get_popular_item()

        # Hourly breakdown
        self.get_hourly_summary()

        # Customer Highlights
        if self.customers:
            best_customer = max(self.customers.items(), key=lambda x: len(x[1]))
            print(f"\n👑  Best Customer: {best_customer[0]} ({len(best_customer[1])} orders)")

            biggest_spender = max(self.customers.items(), key=lambda x: sum(o["total"] for o in x[1]))
            total = sum(o["total"] for o in biggest_spender[1])
            print(f"💰 Biggest Spender: {biggest_spender[0]} ({CURRENCY}{total:.2f})")

    def simulate_busy_hour(self, hour):
        """Simulate orders for a busy hour"""
        print(f"\n⏰ Simulating {hour}:00 hour...")

        # Menu items with prices
        menu = [
            {"name": "Pizza", "price": 8000},
            {"name": "Burger", "price": 6500},
            {"name": "Fries", "price": 3000},
            {"name": "Salad", "price": 3500},
            {"name": "Soda", "price": 900},
            {"name": "Coffee", "price": 1500}
        ]

        # Customers
        customers = ["Tunde", "Tim", "Ali", "Alice", "Dave", "Femi", "Esther",
                     "Ivy", "Hassan"]

        # Generate 5-15 random orders for this hour
        num_orders = random.randint(5, 15)

        for _ in range(num_orders):
            # Pick random customer
            customer = random.choice(customers)

            # Pick 1-3 random items
            num_items = random.randint(1, 3)

            # List of random orders
            items = []
            for _ in range(num_items):
                menu_items = random.choice(menu)
                qty = random.randint(1, 3)
                items.append({
                    "name": menu_items["name"],
                    "price": menu_items["price"],
                    "qty": qty
                })

            # Take the order
            self.take_order(customer, items)


if __name__ == "__main__":
    
    # Test restaurant manager
    print(SEPARATOR)
    print("🏢 TESTING RESTAURANT MANAGER")
    print(SEPARATOR)

    restaurant = RestaurantManager("Python Bistro")

    # Open for business
    restaurant.open_restaurant()

    # Simulate a few hours of business
    restaurant.simulate_busy_hour("12")  # Lunch rush
    restaurant.simulate_busy_hour("13")  # Late lunch
    restaurant.simulate_busy_hour("18")  # Dinner rush
    restaurant.simulate_busy_hour("19")  # Late dinner

    # Check customer history
    restaurant.get_customer_history("Femi")
    restaurant.get_customer_history("Ali")

    # Check hourly summary
    restaurant.get_hourly_summary()

    # Close and generate final report
    restaurant.close_restaurant()