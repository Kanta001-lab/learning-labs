from collections import defaultdict, Counter
from datetime import datetime

CURRENCY = "₦"
SEPARATOR = "=" * 50


class Inventory:
    """
    Attributes:
        stock : dict
            Maps item names to (quantity, price) tuples.

        sales : list
            Chronological list of all sales transactions.
        
        popular_items : Counter
            Tracks total quantity sold of each item for popularity ranking.

        low_stock_alerts : set
            Stores names of items with quantity below restock_threshold.

        restock_threshold : int
            Minimum quantity before triggering low stock alert. Default: 10

    Methods:
        add_item(name, quantity, price)
        sell_item(name, quantity)
        _check_restock_needed(name)
        get_low_stock()
        get_sales_report()
    """

    def __init__(self):
        """Initialize empty inventory system"""
        self.stock = {}
        self.sales = []
        self.popular_items = Counter()
        self.low_stock_alerts = set()
        self.restock_threshold = 10

        print("✅ Inventory System Initialized!\n")

    def add_item(self, name, quantity, price):
        """Add new item or add to existing item's quantity."""

        print(f"\n📦 Adding: {name} (Quantity: {quantity}, Price: {CURRENCY}{price})")

        # If item exists, add to quantity
        if name in self.stock:
            current_qty, current_price = self.stock[name]
            new_qty = current_qty + quantity
            self.stock[name] = (new_qty, current_price)
            print(f"   ✅ Updated {name}: {current_qty} -> {new_qty}")
        else:
            # New item: store as (quantity, price)
            self.stock[name] = (quantity, price)
            print(f"   ✅ New item added: {name}")


        self._check_restock_needed(name)
        return True

    def sell_item(self, name, quantity):
        """Process a sale, update stock, and record transaction."""
        print(f"\n💰 Selling {quantity}x {name}")

        # If item exists
        if name not in self.stock:
            print(f"   ❌ Error: {name} not found in inventory!")
            return False

        # Check if enough stock
        available_qty, price = self.stock[name]
        if available_qty < quantity:
            print(f"   ❌ Error: Only {available_qty} {name} available!")
            return False

        # Update stock
        new_qty = available_qty - quantity
        self.stock[name] = (new_qty, price)
        print(f"   ✅ Stock updated: {available_qty} -> {new_qty}")

        # Record the sale
        sale = {
            "item": name,
            "quantity": quantity,
            "total": price * quantity,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }

        self.sales.append(sale)
        print(f"   ✅ Sale recorded: {CURRENCY}{sale['total']:.2f}")

        # Update popular items counter
        self.popular_items[name] += quantity
        print(f"   ✅ Popularity: {name} now sold {self.popular_items[name]} total")

        self._check_restock_needed(name)
        return True

    def _check_restock_needed(self, name):
        """Private method to check if item needs restock alert."""
        if name in self.stock:
            qty, _ = self.stock[name]
            if qty < self.restock_threshold:
                self.low_stock_alerts.add(name)
                print(f"   ⚠️  ALERT! {name} low stock ({qty} left)!")
                return True
            else:
                # Remove from alerts if stock is sufficient
                self.low_stock_alerts.discard(name)
        return False

    def get_low_stock(self):
        """Display all items that need restocking."""
        print("\n" + SEPARATOR)
        print("📋 LOW STOCK REPORT")
        print(SEPARATOR)

        if not self.low_stock_alerts:
            print("   ✅ All items above threshold")
        else:
            for item in sorted(self.low_stock_alerts):
                qty, price = self.stock[item]
                print(f"   ⚠️  Alert! {item}: {qty} left (Threshold: {self.restock_threshold})")

        print()
        return self.low_stock_alerts

    def get_sales_report(self):
        """Generate comprehensive sales report with statistics."""
        print("\n" + SEPARATOR)
        print("📊 SALES REPORT")
        print(SEPARATOR)

        # Calculate totals
        total_revenue = sum(sale['total'] for sale in self.sales)
        total_items = sum(sale["quantity"] for sale in self.sales)

        print(f"   Total Items Sold: {total_items} sold")
        print(f"   Total Revenue: {CURRENCY}{total_revenue:.2f}")
        print(f"   Number of Transactions: {len(self.sales)}")

        # Popular items:
        print("\nTop Selling Items:")
        for item, count in self.popular_items.most_common(3):
            # Get current stock
            if item in self.stock:
                qty, _ = self.stock[item]
                stock_status = f"({qty} left)"
            else:
                stock_status = "(Out of stock)"
            print(f" {item}: {count} sold {stock_status}")

        # Recent sales
        print("\n Recent Transaction:  (last 5)")
        for sale in self.sales[-5:]:
            print(f" {sale['timestamp']} - {sale['quantity']}x {sale['item']} - {CURRENCY}{sale['total']:.2f}")


        # Inventory value
        print("\n   Current Inventory Value:")
        total_value = sum(qty * price for qty, price in self.stock.values())
        print(f"     {CURRENCY}{total_value:.2f}")

        print(SEPARATOR + "\n")

        return {
            "revenue": total_revenue,
            "items_sold": total_items,
            "transactions": len(self.sales)
        }



if __name__ == "__main__":
    """
    Test the Inventory System with sample data.
    """
    print(SEPARATOR)
    print("TESTING INVENTORY SYSTEM")
    print(SEPARATOR)


    my_store = Inventory()

    # Add items
    print("\n--- ADDING ITEMS ---")
    my_store.add_item("Pizza", 50, 39000)
    my_store.add_item("Burger", 50, 250000)
    my_store.add_item("Fries", 50, 175000)
    my_store.add_item("Soda", 100, 15000)

    # Make sales
    print("\n--- PROCESSING SALES ---")
    my_store.sell_item("Pizza", 45)  # Will trigger low stock alert (5 left)
    my_store.sell_item("Soda", 40)
    my_store.sell_item("Fries", 45)  # Will trigger low stock alert (5 left)
    my_store.sell_item("Burger", 48)  # Will trigger low stock alert (2 left)

    # Check low stock items
    my_store.get_low_stock()

    # Generate full sales report
    my_store.get_sales_report()
