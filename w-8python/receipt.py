def print_receipt(name, food, quantity, price, delivery_charges):
    subtotal = quantity * price
    total = subtotal + delivery_charges

    print("\n=== Food Receipt ===")
    print(f"Customer Name   : {name}")
    print(f"Food Item       : {food}")
    print(f"Quantity        : {quantity}")
    print(f"Price per Item  : RM{price:.2f}")
    print(f"Subtotal        : RM{subtotal:.2f}")
    print(f"Delivery Charges: RM{delivery_charges:.2f}")
    print("---------------------------")
    print(f"Total Amount    : RM{total:.2f}")