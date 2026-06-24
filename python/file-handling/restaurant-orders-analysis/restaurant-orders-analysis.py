import csv
from collections import defaultdict

# CONSTANTS
CURRENCY = "₦"
SEPARATOR = "=" * 50

# =======================================================================
# Task 1: Calculate Total Revenue From Delivered Orders
# =======================================================================


def analyze_restaurant_orders():
    """Calculate revenue and find popular items"""

    total_revenue = 0
    item_sales = {}
    delivered_count = 0

    with open("restaurant_orders.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header row

        print("Analyzing orders..\n")

        for row in reader:
            order_id = int(row[0])
            customer = row[1]
            item = row[2]
            quantity = int(row[3])
            price = float(row[4])
            status = row[6]

            # Counting only delivered orders for revenue
            if status == "delivered":
                order_total = quantity * price
                total_revenue += order_total
                delivered_count += 1

                # Track item popularity
                if item in item_sales:
                    item_sales[item] += quantity
                else:
                    item_sales[item] = quantity

                print(f" ✅ Order #{order_id}: {quantity}x {item} = {CURRENCY}{order_total:.2f}")

    # Calculate average order value
    avg_order_value = total_revenue / delivered_count if delivered_count > 0 else 0

    # Most popular item
    most_popular = max(item_sales, key=item_sales.get)

    print(f"\n SUMMARY:")
    print(f"  Total Revenue: {CURRENCY}{total_revenue:.2f}")
    print(f"  Number of delivered orders: {delivered_count}")
    print(f"  Average Order Value: {CURRENCY}{avg_order_value:.2f}")
    print(f"  Most Popular Item: {most_popular} ({item_sales[most_popular]} sold)")

    return total_revenue, item_sales


# =======================================================================
# Task 2: Group Orders By The Hour
# =======================================================================

def orders_by_date():
    """Create a summary of orders for each date"""
    print(f"\n Analyzing orders by date...\n")
    grouped_orders = defaultdict(list)

    with open("restaurant_orders.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)  # skip header row


        for row in reader:
            order_id = int(row[0])
            customer = row[1]
            item = row[2]
            quantity = int(row[3])
            price = float(row[4])
            date = row[5]
            status = row[6]

            order_total = quantity * price

            grouped_orders[date].append({
                "order_id": order_id,
                "customer": customer,
                "item": item,
                "quantity": quantity,
                "price": price,
                "order_total": order_total,
                "status": status
            })

        for date, orders in grouped_orders.items():
            total_for_day = sum(order['order_total'] for order in orders if order['status'] == 'delivered')
            print(f"\n {date}:")
            print(f"  Total Orders: {len(orders)}")
            print(f"  Revenue: {CURRENCY}{total_for_day:.2f}")

            for order in orders:
                status_emoji = "✅" if order['status'] == 'delivered' else "❌" if order['status'] == 'cancelled' else "🔙"
                print(f"   {status_emoji} Order #{order['order_id']}: {order['quantity']}x {order['item']} ({CURRENCY}{order['order_total']:.2f})")

    return dict(grouped_orders)


# =======================================================================
# Task 3: Find Cancelled Orders
# =======================================================================

def find_cancelled_orders():
    """Find all cancelled orders and calculate potential lost revenue"""

    print("\nAnalyzing cancelled orders...\n")
    cancelled_count = 0
    revenue_lost = 0

    with open("restaurant_orders.csv", "r") as f:
        reader = csv.reader(f)
        header = next(reader)

        for row in reader:
            order_id = int(row[0])
            customer = row[1]
            item = row[2]
            quantity = int(row[3])
            price = float(row[4])
            status = row[6]

            if status == "cancelled":
                order_total = quantity * price
                revenue_lost += order_total
                cancelled_count += 1

                print(f"\n  ❌ Order #{order_id}: {quantity}x {item} = {CURRENCY}{order_total:.2f}")

        print(f"\n📈 SUMMARY:")
        print(f"  Total Revenue Lost: -{CURRENCY}{revenue_lost:.2f}")
        print(f"  Number of cancelled orders: {cancelled_count}")

        return revenue_lost, cancelled_count


if __name__ == "__main__":
    revenue, sales = analyze_restaurant_orders()
    lost_revenue, cancelled_orders = find_cancelled_orders()
    days = orders_by_date()
    for day, orders in days.items():
        print(f"  {day} - {orders}")
