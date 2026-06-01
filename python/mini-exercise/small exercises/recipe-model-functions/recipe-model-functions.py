def make_donuts(glaze_type, sprinkles=False):
    """
    Create a customized donut based on glaze and sprinkles.

    Args:
        glaze_type (str): Type of glaze to add.
                         Options: "chocolate", "caramel", or any other string
        sprinkles (bool, optional): Whether to add rainbow sprinkles.
                                   Defaults to False.

    Returns:
        str: A description of the finished donut with emojis

    Examples:
        >>> make_donuts("chocolate")
        '🍫 plain donut'

        >>> make_donuts("caramel", True)
        '🍮 plain donut with rainbow sprinkles 🌈'

        >>> make_donuts("strawberry")
        '✨ plain donut'
    """

    # Start with base donut (always the same)
    donut = "plain donut"

    # glaze based on ingredient
    if glaze_type == "chocolate":
        donut = "🍫 " + donut
    elif glaze_type == "caramel":
        donut = "🍮 " + donut
    else:
        # Default for any other glaze type
        donut = "✨ " + donut

    # Add sprinkles if requested
    if sprinkles:
        donut = donut + " with rainbow sprinkles 🌈"

    # Return the finished product
    return donut

# TEST THE FUNCTION
# Make different donuts with the SAME recipe
print("=== Making Donuts ===")

donut1 = make_donuts("chocolate")
print(f"Order 1: {donut1}")

donut2 = make_donuts("caramel", sprinkles=True)
print(f"Order 2: {donut2}")

donut3 = make_donuts("strawberry")
print(f"Order 3: {donut3}")
