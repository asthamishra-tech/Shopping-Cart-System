

SALE_ITEMS = {"apple", "banana", "milk"}

cart = []

while True:
    print("\n===== SHOPPING CART MENU =====")
    print("1. Add item")
    print("2. View cart")
    print("3. Check deals")
    print("4. Clear cart")
    print("5. Exit")

    choice = input("Enter your choice: ")

   
    if choice == "1":
        name = input("Enter item name: ").lower()
        price = float(input("Enter item price: "))

        # Tuple containing item name and price
        item = (name, price)

        cart.append(item)

        print(f"{name} added to cart.")

    #  View cart and calculate total
    elif choice == "2":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            print("\n===== YOUR CART =====")

            total = 0

            for name, price in cart:
                print(f"Item: {name} | Price: ₹{price:.2f}")
                total += price

            print("---------------------")
            print(f"Number of items: {len(cart)}")
            print(f"Total cost: ₹{total:.2f}")

    # Check deals
    elif choice == "3":
        if len(cart) == 0:
            print("Your cart is empty.")
        else:
            # Extract item names from tuples
            cart_items = []

            for name, price in cart:
                cart_items.append(name)

            # Convert list to set to get unique item names
            cart_set = set(cart_items)

            # Find common items between cart and sale items
            sale_items_in_cart = cart_set & SALE_ITEMS

            print(f"\nUnique items in cart: {len(cart_set)}")

            if sale_items_in_cart:
                print("Sale items in your cart:")
                print(sale_items_in_cart)
            else:
                print("No sale items in your cart.")

    #  Clear cart
    elif choice == "4":
        cart.clear()
        print("Cart cleared successfully.")

    #  Exit
    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Please select 1-5.")