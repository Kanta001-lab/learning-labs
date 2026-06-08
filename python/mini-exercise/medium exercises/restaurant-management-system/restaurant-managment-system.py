from collections import defaultdict, Counter
from datetime import datetime

# Constants
SEPARATOR = "=" * 50
CURRENCY = "₦"


class RestaurantManager:
    """
    Manages restaurant operations including orders, customers, and statistics.

    This class serves as the core of the restaurant management system.

    Attributes:
        orders: (list)
            A chronological list of all the orders.

        customers: defaultdict(list)
            Maps customer names to their order history.

        daily_stats : dict
            Contains aggregated statistics:

    Notes:
        - Timestamps are auto-generated in 24-hour format (HH:MM)
        - Customer names are case-sensitive
        - Item counts use Counter.most_common() for ranking
    """

    def __init__(self):
        """Initialize empty restaurant management system."""
        # List of all orders
        self.orders = []

        # Customer order history
        self.customers = defaultdict(list)

        # Daily aggregated statistics
        self.daily_stats = {
            "revenue": 0,
            "orders_count": 0,
            "popular_items": Counter()
        }

    def add_order(self, customer_name, items, total):
        """
       Add a new order and update restaurant statistics.

        Args:
            customer_name : str
                Name of the customer placing the order.
            items: list of str
                List of items ordered.
            totals: float
                Total cost of the orders in current unit.

        Returns:
            None 

        Side Effects:
            - Updates orders list
            - Updates customer history
            - Updates daily statistics
 
        Complexity:
            O(n) where n is the number of items.
        """

        order = {
            "id": len(self.orders) + 1,
            "customer": customer_name,
            "items": items,
            "totals": total,
            "timestamp": datetime.now().strftime("%H:%M")
        }

        # Update data structures
        self.orders.append(order)
        self.customers[customer_name].append(order)

        # Update statistics
        self.daily_stats["revenue"] += total
        self.daily_stats["orders_count"] += 1

        # popularity ranking
        for item in items:
            self.daily_stats["popular_items"][item] += 1

    def get_customer_history(self, customer_name):
        """
        Retrieve all orders placed by a specific customer.

        Args:
            customer_name: str
                Name of the customer to look up

        Returns:
            list
                List of order dictionaries for that customer.
        """
        return self.customers.get(customer_name, [])

    def get_hourly_summary(self):
        """
        Group orders by the hours they were placed.

        Returns:
            dict
                Dictionary mapping hour strings to list of orders.
        """
        hourly = defaultdict(list)

        for order in self.orders:
            hour = order["timestamp"].split(":")[0]
            hourly[hour].append(order)

        return dict(hourly)

    def print_dashboard(self):
        """Display a formatted restaurant dashboard with all key metrics."""

        print("\n" + SEPARATOR)
        print(" Restaurant Dashboard")
        print(SEPARATOR)

        print(f"\n Total Orders: {self.daily_stats['orders_count']}")
        print(f"  Total Revenue: {CURRENCY}{self.daily_stats['revenue']:.2f}")

        print(f"\n Top Selling Items:")
        for order, count in self.daily_stats["popular_items"].most_common(3):
            print(f"  {order}: {count} sold")

        print("\n Customer Activity:")
        for customer, order in list(self.customers.items())[:5]:  # Top 5 customers
            print(f"  {customer}: {len(order)}")

        print("\n Hourly Distribution:")
        hourly = self.get_hourly_summary()
        for hour in sorted(hourly.keys()):
            print(f"   {hour}:00 {len(hourly[hour])} orders")

        print("\n" + SEPARATOR)



if __name__ == "__main__":

    """
    Create a restaurant, add orders,and view dashboard
    """

    # Create restaurant instance
    restaurant = RestaurantManager()

    # Add orders
    restaurant.add_order("Femi", ["Pizza", "Coke"], 8500)
    restaurant.add_order("John", ["Salad", "Water"], 4500)
    restaurant.add_order("Zoe", ["Burger", "Pepsi"], 6500)
    restaurant.add_order("Caleb", ["Pizza", "Water"], 8200)
    restaurant.add_order("Emma", ["Salad", "Coke"], 4700)
    restaurant.add_order("Hassan", ["Pizza", "Coke"], 8500)

    # Display dashboard
    restaurant.print_dashboard()

    """
    Customer History Lookup
    """
   
    print("\nCustomer Order History")
    print(SEPARATOR)

    femi_orders = restaurant.get_customer_history("Femi")
    print(f"Jack's orders: {len(femi_orders)}")
    for order in femi_orders:
        print(f" Order #{order['id']}: {order['items']} - {CURRENCY}({order['totals']:.2f})")

    """
    Hourly Breakdown
    """
   
    print("\nHourly Breakdown")
    print(SEPARATOR)

    hourly = restaurant.get_hourly_summary()
    for hour, orders in hourly.items():
        print(f" {hour}:00 - {len(orders)}")

    """
    Adding More Orders Dynamically
    """
   
    print("\nAdding Orders in Real-Time")
    print(SEPARATOR)

    # Simulate a busy hour
    new_orders = [
        ("Femi", ["Burger", "Fries"], 7200,),
        ("Zoe", ["Pizza"], 8000,),
        ("Jane", ["Salad", "Coke"], 4500,)
    ]

    for customer, items, total in new_orders:
        restaurant.add_order(customer, items, total)
        print(f" Added order for {customer}: {items}")

    print(f"\nUpdated total orders: {restaurant.daily_stats['orders_count']}")
    print(f"Updated revenue: {CURRENCY}{restaurant.daily_stats['revenue']:.2f}")
