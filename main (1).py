# BREWTRACK: COFFEE SHOP ORDERING SYSTEM

orders = []
order_number = 1001

menu = {
    "1": ("Americano", 80),
    "2": ("Cafe Latte", 100),
    "3": ("Cappuccino", 110),
    "4": ("Mocha", 120),
    "5": ("Caramel Macchiato", 130)
}

size_prices = {
    "Small": 0,
    "Medium": 20,
    "Large": 40
}


def display_menu():
    print("\n===== COFFEE MENU =====")
    for key, item in menu.items():
        print(f"{key}. {item[0]} - PHP {item[1]}")
    print("=======================")


def create_order():
    global order_number

    customer = input("Enter customer name: ")
    display_menu()

    choice = input("Choose a drink (1-5): ")

    if choice not in menu:
        print("Invalid drink selection!")
        return

    drink, price = menu[choice]

    print("\nSizes: Small, Medium, Large")
    size = input("Choose size: ").capitalize()

    if size not in size_prices:
        print("Invalid size!")
        return

    sweetness = input("Sweetness level (0%, 25%, 50%, 75%, 100%): ")

    if sweetness not in ["0%", "25%", "50%", "75%", "100%"]:
        print("Invalid sweetness level!")
        return

    customization = input("Other customization (None if none): ")

    quantity = input("Enter quantity: ")

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity!")
        return

    quantity = int(quantity)
    total = (price + size_prices[size]) * quantity

    order = {
        "number": order_number,
        "customer": customer,
        "drink": drink,
        "size": size,
        "sweetness": sweetness,
        "customization": customization,
        "quantity": quantity,
        "total": total,
        "status": "Preparing"
    }

    orders.append(order)

    print("\n===== ORDER SUMMARY =====")
    print("Order Number:", order_number)
    print("Customer:", customer)
    print("Drink:", drink)
    print("Size:", size)
    print("Sweetness:", sweetness)
    print("Customization:", customization)
    print("Quantity:", quantity)
    print(f"Total: PHP {total:.2f}")
    print("Status: Preparing")
    print("=========================")

    order_number += 1


def view_orders():
    print("\n===== ALL ORDERS =====")

    if not orders:
        print("No orders available.")
        return

    for order in orders:
        print(f"\nOrder Number: {order['number']}")
        print(f"Customer: {order['customer']}")
        print(f"Drink: {order['drink']}")
        print(f"Size: {order['size']}")
        print(f"Sweetness: {order['sweetness']}")
        print(f"Quantity: {order['quantity']}")
        print(f"Total: PHP {order['total']:.2f}")
        print(f"Status: {order['status']}")


def update_status():
    number = input("Enter order number: ")

    for order in orders:
        if str(order["number"]) == number:
            print("\n1. Preparing")
            print("2. Ready for Pickup")
            print("3. Completed")

            choice = input("Choose new status: ")

            statuses = {
                "1": "Preparing",
                "2": "Ready for Pickup",
                "3": "Completed"
            }

            if choice in statuses:
                order["status"] = statuses[choice]
                print("Order status updated successfully!")
                print("New Status:", order["status"])
            else:
                print("Invalid status selection!")

            return

    print("Order not found!")


while True:
    print("\n===== BREWTRACK SYSTEM =====")
    print("1. Create Customer Order")
    print("2. View All Orders")
    print("3. Update Order Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_order()
    elif choice == "2":
        view_orders()
    elif choice == "3":
        update_status()
    elif choice == "4":
        print("Thank you for using BrewTrack!")
        break
    else:
        print("Invalid choice. Please try again.")
