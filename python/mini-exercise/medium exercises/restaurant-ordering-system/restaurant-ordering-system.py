from collections import defaultdict
from datetime import datetime

# CONSTANTS
CURRENCY = "₦"
SEPARATOR1 = "=" * 40
SEPARATOR2 = "-" * 40


class MenuItem:
    """
    Represents a single item on the menu, each item has a name, price, category,
    prep_time.

    Attributes
        name: (str)
            Stores item name e.g., "Margherita Pizza", "Garlic Bread"

        price: (int)
            Item price e.g., 14.99

        category: (str)
            Used for kitchen station assignment

        prep_time: (int)
            How many minutes to prepare

        orders_count: (int)
            Incremented each time its ordered

    Methods
        str():
            Returns item name and price

    """

    def __init__(self, name, price, category, prep_time):
        self.name = name
        self.price = price
        self.category = category
        self.prep_time = prep_time
        self.orders_count = 0

    def __str__(self):
        return f"{self.name}  {CURRENCY}{self.price:.2f}"


class Order:
    """
    Represents a customer order it stores unique id, customer name and table. it
    also stores a list of items, timestamsp and order status.

    Attributes
        order_id: (int)

        customer_name: (str)

        items: (list)
            List of items (each as tuple: (MenuItem, quantity)

        order_time: (datetime)
            Timestamp when the order was created

        status: (str)
            Current status (pending -> preparing -> ready -> served)


    Methods
        add_item(menu_item, quantity=1)
            - Adds an item to the order's item list
            - It also increments the MenuItems orders_count

        calculate_total()
            - Uses a generator expression inside sum()
            - Multiplies each item's price by its quantity
            - Returns total order value

        estimated_prep_time()
            - Sum prep time x quantity for all items
            - Helps the kitchen to know how long this order will take

        receipt()
            - Builds a nicely formatted receipt string
            - Uses strftime() to formate time
            - Returns multi-line string
    """

    def __init__(self, order_id, customer_name, table_number):
        self.order_id = order_id
        self.customer_name = customer_name
        self.table_number = table_number
        self.items = []
        self.order_time = datetime.now()
        self.status = "pending"

    def add_item(self, menu_item, quantity=1):
        """
        Add an item to the order

        Args:
            menu_item (list): items list
            quantity (int): item quantity

        Example:
            >>> # Add items to order
            >>> order1.add_item(restaurant.menu[2], 2)  # 2 Pizzas
            >>> order1.add_item(restaurant.menu[7], 3)  # 3 Drinks
        """
        self.items.append((menu_item, quantity))
        menu_item.orders_count += quantity
        print(f"  ✅ Added {quantity}x {menu_item.name}")

    def calculate_total(self):
        """
        Calculate order total

        Returns:
            Total order value
        """
        return sum(item.price * qty for item, qty in self.items)

    def estimated_prep_time(self):
        """
        Estimated total preparation time

        Returns:
            Sum prep Time x quantity for all items
        """
        return sum(item.prep_time * qty for item, qty in self.items)

    def receipt(self):
        """
        Generates receipt text

        Returns
            (str): Multi-line string.
        """
        lines = []
        lines.append(SEPARATOR1)
        lines.append(f"ORDERS #{self.order_id} - Table {self.table_number}")
        lines.append(f"Customer: {self.customer_name}")
        lines.append(f"Time: {self.order_time.strftime('%H:%M')}")
        lines.append(SEPARATOR2)

        for item, qty in self.items:
            lines.append(f"{qty}x {item.name:20} {CURRENCY}{item.price * qty:.2f}")

        lines.append(SEPARATOR2)
        lines.append(f"{'TOTAL:20'} {CURRENCY}{self.calculate_total():.2f}")
        lines.append(SEPARATOR1)
        lines.append(f"Status: {self.status.upper()}")
        lines.append(f"Est. prep time: {self.estimated_prep_time()} minutes")

        return "\n".join(lines)


class Kitchen:
    """
    Manages food preparation. tracking orders being prepared, ready to serve
    and mapping items categories to their stations.

    Attributes
        name: (str)
            Kitchen name

        current_orders: (list)
            Orders being prepared

        completed_orders: (list)
            Completed orders ready to serve

        stations: (Dict):
            Mapping order category to their station


    Methods
        receive_order(order):
            - Called when restaurants submits an order to the kitchen
            - Updates order status to "preparing"
            - Adds order to current orders
            - Groups items by category using defaultdict(list)
            - Prints which station will handle items

        complete_order(order_id):
            - Simulates finishing an order
            - Finds order in current orders by ID
            - Updates status to "ready"
            - Moves order from current orders to completed orders
            - Returns True if found, False otherwise
    """

    def __init__(self, name):
        self.name = name
        self.current_orders = []
        self.completed_orders = []
        self.stations = {
            "appetizer": "Cold Station",
            "main": "Hot Station",
            "dessert": "Pastry Station",
            "drink": "Bar Station"
        }

    def receive_order(self, order):
        """Kitchen gets a new order"""

        print(f"\n{self.name} received Order #{order.order_id}")
        order.status = "preparing"
        self.current_orders.append(order)

        # Group items by the category for station assignment
        by_station = defaultdict(list)
        for item, qty in order.items:
            by_station[item.category].append((item, qty))

            for station, items in by_station.items():
                print(f" → {self.stations[station]}: {len(items)} items")


    def complete_order(self, order_id):
        """Mark order as ready"""
        for order in self.current_orders:
            if order.order_id == order_id:
                order.status = "ready"
                self.current_orders.remove(order)
                self.completed_orders.append(order)
                print(f"\n Order #{order_id} is READY!")
                return True
        return False


class Restaurant:
    """
    The restaurant is the center of control, with restaurant attributes
    such as managing the menu, orders and submitting orders to the
    kitchen.

    Attributes:
        menu: (list)
            List of menu items

        orders: (list)
            List of all orders

        kitchen: (class)
            A kitchen object

        next_order_id: (int)
            Auto-incrementing ID


    
    Methods
        _setup_menu(): private method
            - Initializes the menu with default items
            - Called automatically when restaurant is created

        show_menu():
            - Groups menu items by category
            - Prints a nicely formatted menu
            - Uses dictionary to group items

        create_order(customer_name, table_number):
            - Creates a new order object with next available ID
            - Adds it to the restaurant's orders list
            - Returns the order object for further manipulation

        submit_order(order):
            - Delegates to kitchens receive_order()

        get_order_status(order_id):
            - Searches for order by ID
            - Prints current status
            - Returns status string | (None)

        daily_report()
            - Generates end-of-day statistics
            - Uses orders_count from each MenuItem top sellers
            - Shows kitchen performance metrics
    """

    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []
        self.kitchen = Kitchen(f"{name} Kitchen")
        self.next_order_id = 1

        # Initialize with default menu
        self._setup_menu()

    def _setup_menu(self):
        """Add default menu items"""
        self.menu.append(MenuItem("Garlic Bread", 5500, "appetizer", 5))
        self.menu.append(MenuItem("Caesar Salad", 6500, "appetizer", 7))
        self.menu.append(MenuItem("Margherita Pizza", 11000, "main", 12))
        self.menu.append(MenuItem("Spaghetti Bolognese", 9800, "main", 15))
        self.menu.append(MenuItem("Grilled Salmon", 10000, "main", 18))
        self.menu.append(MenuItem("Cheesecake", 5500, "dessert", 5))
        self.menu.append(MenuItem("Chocolate Brownie", 5500, "dessert", 4))
        self.menu.append(MenuItem("Soft Drink", 1100, "drink", 2))
        self.menu.append(MenuItem("Coffee", 1100, "drink", 3))

    def show_menu(self):
        """Display the menu by category"""
        print(f"\n📋 {self.name} MENU")
        print(SEPARATOR1)

        # Group by category
        categories = {}
        for item in self.menu:
            if item.category not in categories:
                categories[item.category] = []
            categories[item.category].append(item)

        # print each category
        for category, items in categories.items():
            print(f"\n{category.upper()}:")
            for item in items:
                print(f"  {item.name:25} {CURRENCY}{item.price:.2f}")

    def create_order(self, customer_name, table_number):
        """
        Creates new order object(ID, customer_name, table_no)

        Returns:
            order1 object

        Example:
          >>> # Create first order
          >>> order1 = restaurant.create_order("Ali", 5)
        """
        order = Order(self.next_order_id, customer_name, table_number)
        self.orders.append(order)
        self.next_order_id += 1
        print(f"\n Order #{order.order_id} created for {customer_name} (Table {table_number})")
        return order

    def submit_order(self, order):
        """Send order to kitchen"""
        return self.kitchen.receive_order(order)

    def get_order_status(self, order_id):
        """Order Status """
        for order in self.orders:
            if order.order_id == order_id:
                print(f"\n Order #{order_id} status: {order.status.upper()}")
                return order.status
        print(f"❌ Order #{order_id} not found")
        return None

    def daily_report(self):
        """Generate end-of-day report"""
        print("\n" + SEPARATOR1)
        print(f"📊 {self.name} - DAILY REPORT")
        print(SEPARATOR1)

        total_orders = len(self.orders)
        total_revenue = sum(order.calculate_total() for order in self.orders)

        print(f"Total Orders: {total_orders}")
        print(f"Total Revenue: {CURRENCY}{total_revenue:.2f}")

        # Popular items (orders_count from MenuItem)
        print("\n🏆 TOP SELLING ITEMS:")
        popular = sorted(self.menu, key=lambda x: x.orders_count, reverse=True)[:5]
        for item in popular:
            print(f"  {item.orders_count:3d}x {item.name}")

        # Kitchen performance
        print(f"\n Kitchen Performance:")
        print(f" Orders completed: {len(self.kitchen.completed_orders)}")
        print(f" Orders in progress: {len(self.kitchen.current_orders)}")


if __name__ == "__main__":
   
    restaurant = Restaurant("Python Bistro")

    # Show menu
    restaurant.show_menu()

    # first order
    order1 = restaurant.create_order("Hassan Samir", 5)

    # Add items to order
    order1.add_item(restaurant.menu[2], 2)  # 2 Pizzas
    order1.add_item(restaurant.menu[7], 3)  # 3 Soft Drinks

    # Show receipt
    print(order1.receipt())

    # Submit order to kitchen
    restaurant.submit_order(order1)

    # second order with different items
    order2 = restaurant.create_order("Ali Salihu", 3)
    order2.add_item(restaurant.menu[3], 1)  # Spaghetti
    order2.add_item(restaurant.menu[4], 1)  # Salmon
    order2.add_item(restaurant.menu[5], 2)  # Cheesecake
    order2.add_item(restaurant.menu[8], 2)  # Coffee
    restaurant.submit_order(order2)

    # Check order status
    restaurant.get_order_status(1)

    # Complete an order
    restaurant.kitchen.complete_order(1)

    # Daily report
    restaurant.daily_report()