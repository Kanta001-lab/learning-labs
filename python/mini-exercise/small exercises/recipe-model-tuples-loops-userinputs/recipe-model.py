# CONSTANTS
CURRENCY = "₦"

def calculate_final_price(base_price, size_multiplier):
    """Calculate the final price after applying size multiplier."""
    total_price = base_price * size_multiplier
    return round(total_price, 2)

# MAIN PROGRAM
def main():
    """Main ordering system function"""

    print("==== PIZZA ORDER SYSTEM ====")
    print(f"Currency: {CURRENCY}\n")

    # dictionary mapping numbers to pizza types
    PIZZA_TYPES = {
        "1": ("Classic Pizza", 500),
        "2": ("Beef Lovers", 700),
        "3": ("Cheese Explosion", 600),
        "4": ("Garden Fresh", 400)
    }

    # Display pizza menu using for loop
    print("📋 PIZZA MENU:")
    print("-" * 30)
    for key, (pizza_name, pizza_price) in PIZZA_TYPES.items():
        print(f"  {key}. {pizza_name} - {pizza_price}{CURRENCY}")
    print("-" * 30)

    # Get pizza choice with input validation
    while True:
        pizza_choice = input("\nEnter pizza number (1-4): ").strip()

        if pizza_choice in PIZZA_TYPES:
            pizza_name, pizza_price = PIZZA_TYPES[pizza_choice]
            print(f"  ✅ Selected: {pizza_name}")
            break  
        else:
            print("  ❌ Invalid input! Please enter a number from 1 to 4")

    # dictionary mapping numbers to pizza sizes
    PIZZA_SIZE = {
        "1": ("Small", 0.5),
        "2": ("Medium", 1.0),
        "3": ("Large", 1.5)
    }

    # Display size menu using for loop
    print("\n📏 SIZE OPTIONS:")
    print("-" * 30)
    for key, (size_name, size_multiplier) in PIZZA_SIZE.items():
        multiplier_text = f"x{size_multiplier}"
        print(f"  {key}. {size_name} - {multiplier_text}")
    print("-" * 30)

    # Get size choice with input validation
    while True:
        size_choice = input("\nEnter size number (1-3): ").strip()

        if size_choice in PIZZA_SIZE:
            size_name, size_multiplier = PIZZA_SIZE[size_choice]
            print(f"  ✅ Selected: {size_name}")
            break 
        else:
            print("  ❌ Invalid input! Please enter a number from 1 to 3")

    # Calculate final price using function
    final_price = calculate_final_price(pizza_price, size_multiplier)

    # Display order summary
    print("\n" + "=" * 40)
    print("📖 ORDER SUMMARY")
    print("=" * 40)
    print(f"  Pizza:     {pizza_name}")
    print(f"  Size:      {size_name} (x{size_multiplier})")
    print(f"  Base price: {pizza_price:.2f}{CURRENCY}")
    print("-" * 40)
    print(f"  TOTAL:     {final_price:.2f}{CURRENCY}")
    print("=" * 40)
    print("\n  Thank you for your order! 🍕")
    print("  Enjoy your pizza!\n")


if __name__ == "__main__":
    main()
