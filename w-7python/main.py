from food_order import calculate_total
def main():
    try:
        price = float(input("Price (RM):"))
         quantity = int(input("Quantity:"))

         total = calculate_total(price, quantity)
         print(f"Total Payment = RM {total:.2f}")
         except ValueError as e:
            print(f"Invalid input: {e}")
if _name_ == "_main_":
    main()            
