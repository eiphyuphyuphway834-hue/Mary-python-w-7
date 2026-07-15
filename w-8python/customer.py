def get_customer():
    print("=== Customer Information ===")

    name = input("Enter your name: ")
    food = input("Enter food item: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    if quantity > 5:
        delivery_charges = 0
    else:
        delivery_charges = 5.0

    return name, food, quantity, price, delivery_charges