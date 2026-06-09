# Data structures
from collections import Counter

MC_MENU = {
    "1": ("Egg McMuffin", 800),
    "2": ("Sausage Burrito", 500),
    "3": ("Mc cafe Iced coffee", 400),
    "4": ("Big Mac", 1500)
}

MC_SIZE = {
    "1": ("Small", 0.5),
    "2": ("Medium", 1.0),
    "3": ("Large", 1.5)
}

# Sample orders
orders = [
    ("1", "2"),  # Order 1: Egg McMuffin
    ("2", "3"),  # Order 2: Sausage Burrito, Large
    ("3", "1"),  # Order 3: Mc cafe Iced coffee, Small
    ("4", "2"),  # Order 4: Big Mac, Medium
    ("1", "3")   # Order 5: Egg McMuffin, Large
]

# Constants
CURRENCY = "₦"
SEPARATOR = "=" * 50

def process_order(item_code, size_code):
    """Process single order and return total"""
    item_name, base_price = MC_MENU[item_code]
    size_name, multiplier = MC_SIZE[size_code]
    total = base_price * multiplier
    return item_name, size_name, total

def display_statistics(total_revenue, item_counts, size_counts, order_totals):
    """Display all statistics"""
    print(SEPARATOR)
    print(" STATISTICS")
    print(SEPARATOR)

    print(f"\nTotal Revenue: {total_revenue:.2f}{CURRENCY}")
    print(f"Total Orders: {len(order_totals)} sold")

    print("\nItems sold:")
    for item, count in item_counts.items():
        print(f" {item}: {count}")

    print("\nMost popular:")
    if item_counts:
        most_pop = max(item_counts.items(), key=lambda x: x[1])
        print(f" Most Popular: {most_pop[0]} with {most_pop[1]} orders")

    if size_counts:
        most_pop = max(size_counts.items(), key=lambda x: x[1])
        print(f" Most Popular Size: {most_pop[0]}")

    if order_totals:
        average_value = sum(order_totals) / len(order_totals)
        print(f"\nAverage Value: {average_value:.2f}{CURRENCY}")

    print(f"All orders Processed")

def run_factory(order):
    """Main program"""
    item_count = Counter()
    size_counts  = Counter()
    total_revenue = 0
    order_totals = []

    for order_no, (item_code, size_code) in enumerate(order, 1):
        item_name, size_name, total = process_order(item_code, size_code)
        order_totals.append(total)
        total_revenue += total

        print(f"Order#{order_no}: Ordered - {item_name} size - {size_name}")
        item_count[item_name] += 1
        size_counts[size_name] += 1

    print()
    display_statistics(total_revenue, item_count, size_counts, order_totals)


if __name__ == "__main__":
    run_factory(orders)
