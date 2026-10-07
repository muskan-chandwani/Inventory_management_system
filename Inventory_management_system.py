
products = []


# 1. ADD PRODUCT
def add_product():
    print("\n--- ADD PRODUCT ---")

    product_id = input("Enter Product ID: ")

    # Check if ID already exists
    for product in products:
        if product["id"] == product_id:
            print("Product ID already exists!")
            return

    name = input("Enter Product Name: ")

    try:
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
    except ValueError:
        print("Please enter a valid number for quantity and price.")
        return

    product = {
        "id": product_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }

    products.append(product)

    print("Product added successfully!")


# 2. UPDATE PRODUCT
def update_product():
    print("\n--- UPDATE PRODUCT ---")

    product_id = input("Enter Product ID to update: ")

    for product in products:
        if product["id"] == product_id:

            print("\nProduct found!")
            print("Current Name:", product["name"])
            print("Current Quantity:", product["quantity"])
            print("Current Price:", product["price"])

            new_name = input("Enter New Product Name: ")

            try:
                new_quantity = int(input("Enter New Quantity: "))
                new_price = float(input("Enter New Price: "))
            except ValueError:
                print("Please enter valid quantity and price.")
                return

            product["name"] = new_name
            product["quantity"] = new_quantity
            product["price"] = new_price

            print("Product updated successfully!")
            return

    print("Product not found!")


# 3. DELETE PRODUCT
def delete_product():
    print("\n--- DELETE PRODUCT ---")

    product_id = input("Enter Product ID to delete: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("Product deleted successfully!")
            return

    print("Product not found!")


# 4. SEARCH PRODUCT
def search_product():
    print("\n--- SEARCH PRODUCT ---")

    search_name = input("Enter Product Name to search: ").lower()

    found = False

    for product in products:
        if search_name in product["name"].lower():

            print("\nProduct Found!")
            print("Product ID:", product["id"])
            print("Product Name:", product["name"])
            print("Quantity:", product["quantity"])
            print("Price:", product["price"])

            found = True

    if not found:
        print("Product not found!")


# 5. GENERATE INVENTORY REPORT
def inventory_report():
    print("\n========== INVENTORY REPORT ==========")

    if len(products) == 0:
        print("No products available.")
        return

    total_products = len(products)
    total_quantity = 0
    total_value = 0

    print("\nID\tName\t\tQuantity\tPrice\t\tTotal Value")
    print("-" * 70)

    for product in products:

        product_value = product["quantity"] * product["price"]

        total_quantity += product["quantity"]
        total_value += product_value

        print(
            product["id"],
            "\t",
            product["name"],
            "\t\t",
            product["quantity"],
            "\t\t",
            product["price"],
            "\t\t",
            product_value
        )

    print("-" * 70)

    print("Total Different Products:", total_products)
    print("Total Quantity:", total_quantity)
    print("Total Inventory Value:", total_value)


# MAIN MENU
while True:

    print("\n")
    print("======================================")
    print("     INVENTORY MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Search Product")
    print("5. Generate Inventory Report")
    print("6. Exit")
    print("======================================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_product()

    elif choice == "2":
        update_product()

    elif choice == "3":
        delete_product()

    elif choice == "4":
        search_product()

    elif choice == "5":
        inventory_report()

    elif choice == "6":
        print("\nThank you for using Inventory Management System!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")