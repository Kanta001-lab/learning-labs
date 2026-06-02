def make_pizza(pizza_type, pizza_topping, pineapple=False):
    """
    Creates a customized pizza description using dictionary lookups.

    Args:
        pizza_type (str): Type of pizza base.
                         Options: "classic", "beef_pizza", "cheese_pizza",
                                 "vegan_pizza", or any custom type
                                 
        pizza_topping (str): Topping to add.

        pineapple (bool, optional): Whether to add pineapple.
                                   Defaults to False.

    Returns:
        str: A formatted description of the finished pizza with emojis

    Examples:
        >>> make_pizza("classic", "basil")
        '🍅 pizza with 🌿 toppings'

        >>> make_pizza("vegan_pizza", "mushrooms", pineapple=True)
        '🍲 pizza with 🍄 toppings and pineapple 🍍'

        >>> make_pizza("exotic_pizza", "kelp")
        'special pizza with special toppings'

        >>> make_pizza("cheese_pizza", "egg")
        '🧀 pizza with 🥚 toppings'

    Note:
        Unknown pizza types or toppings get "special" fallbacks,
        just like a real pizza shop improvising with customer requests!
    """

    # dictionary mapping pizza types to emojis
    type_map = {
        "classic": "🍅 pizza",
        "beef_pizza": "🥩 pizza",
        "cheese_pizza": "🧀 pizza",
        "vegan_pizza": "🍲 pizza"
    }

    # toppings menu
    toppings_map = {
        "mushrooms": "🍄 toppings",
        "basil": "🌿 toppings",
        "shrimp": "🍤 toppings",
        "egg": "🥚 toppings"
    }

    # Look up values with fallbacks for unknown items
    # .get(key, default) returns default if key doesn't exist
    pizza_display = type_map.get(pizza_type, "special pizza")
    toppings_display = toppings_map.get(pizza_topping, "special toppings")

    # Add pineapple if requested
    if pineapple:
        pineapple_display = "and pineapple 🍍"
    else:
        pineapple_display = ""

    # Build the final description
    if pineapple_display:
        return f"{pizza_display} with {toppings_display} {pineapple_display}"
    else:
        return f"{pizza_display} with {toppings_display}"


#  TEST THE FUNCTION 
print("=== ORDERING PIZZAS ====")
print("=" * 40)

# Test 1: Classic pizza with basil
order1 = make_pizza("classic", "basil")
print(f"Order 1: {order1}")

# Test 2: Vegan pizza with mushrooms and pineapple
order2 = make_pizza("vegan_pizza", "mushrooms", pineapple=True)
print(f"Order 2: {order2}")

# Test 3: Unknown pizza type (uses fallback)
order3 = make_pizza("exotic_pizza", "kelp")
print(f"Order 3: {order3}")

# Test 4: Cheese pizza with egg
order4 = make_pizza("cheese_pizza", "egg")
print(f"Order 4: {order4}")

print("=" * 40)
print("\n🍕 All pizzas served! 🍕")