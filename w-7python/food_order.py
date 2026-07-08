def calculate_total(price, quantity):
    # Validate the price
    if price < 0:
        raise ValueError("invalid price")

    # Validate the quantity
    if quantity < 0:
        raise ValueError("invalid quantity")

    return price * quantity