class Shoe:
    # Initialize the Shoe object with attributes
    # for country, code, product, cost, and quantity
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    # Get the cost of the shoe
    def get_cost(self):
        return self.cost

    # Get the quantity of the shoe
    def get_quantity(self):
        return self.quantity

    # Get the new quantity of the shoe
    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    # String representation of the Shoe object
    def __str__(self):
        return (
            f"Country: {self.country},\n"
            f"Code: {self.code},\n"
            f"Product: {self.product},\n"
            f"Quantity: {self.quantity}"
        )


# List to store Shoe objects
shoe_list = []


# Read shoe data from a file and populate the shoe_list
def read_shoes_data():
    global shoe_list
    shoe_list.clear()
    try:
        with open('inventory.txt', 'r') as file:
            next(file)  # Skip the header
            for line in file:
                country, code, product, cost, quantity = (
                    line.strip().split(',')
                )
                shoe = Shoe(country, code, product, float(cost), int(quantity))
                shoe_list.append(shoe)
        print("Shoe data loaded successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except ValueError as e:
        print(f"Error occurred: {e}.")


# Capture shoe information from user input and add it to the shoe_list
def capture_shoes():
    country = input("Enter the country: ")
    code = input("Enter the code: ")
    product = input("Enter the product: ")
    cost = input("Enter the cost: ")
    quantity = input("Enter the quantity: ")
    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    with open("inventory.txt", "a") as file:
        file.write(f"\n{country}, {code}, {product}, {cost}, {quantity}")
        print("The shoe information has been added.")


# View all shoes in the shoe_list
def view_all():
    if shoe_list:
        print("\nCurrent Shoe Inventory: ")
        print("Country / Code / Product / Cost/ Quantity")
        print("-" * 40)
        for shoe in shoe_list:
            print(f"{shoe.country} / {shoe.code}/ {shoe.product}/ "
                  f"{shoe.cost}/ {shoe.quantity}")
    else:
        print("Your shoe request is not in the list.")


# Update the inventory.txt file after modification
def update_inventory_file():
    try:
        with open('inventory.txt', 'w') as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoe_list:
                file.write(f"{shoe.country},{shoe.code},"
                           f"{shoe.product},{shoe.get_cost()},"
                           f"{shoe.get_quantity()}\n")
        print("Inventory file updated successfully.")
    except Exception as e:
        print(f"Error updating file: {e}")


# Restock the shoe with the lowest quantity
def re_stock():
    if len(shoe_list) == 0:
        print("No shoes to restock.")
        return

    lowest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity < lowest_shoe.get_quantity():
            lowest_shoe = shoe

    print(f"The shoe with the lowest stock is: {lowest_shoe}")
    try:
        additional_stock = int(input("Enter quantity to add: "))
        lowest_shoe.set_quantity(lowest_shoe.get_quantity() + additional_stock)
        print(f"Stock updated: {lowest_shoe.product}")

        update_inventory_file()
        print("Inventory file updated successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number")


# Search for a shoe by code
def search_shoe():
    if not shoe_list:
        print("No shoe data available.")
        return

    code = input("Enter the shoe code: ")
    found_shoe = None
    for shoe in shoe_list:
        if shoe.code == code:
            found_shoe = shoe
            break

    if found_shoe:
        print(f"Shoe found: {found_shoe}")
    else:
        print("Shoe was not found.")


# Calculate the value per item in the shoe_list
def value_per_item():
    if not shoe_list:
        print("No shoe data available")
        return
    print("\nShoe Inventory Values:")
    print("Product/ Value: ")
    print("-" * 30)
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} / £{value:.2f}")


# Find the shoe with the highest quantity
def highest_qty():
    if not shoe_list:
        print("No shoe data available.")
        return

    highest_shoe = shoe_list[0]
    for shoe in shoe_list:
        if shoe.quantity > highest_shoe.get_quantity():
            highest_shoe = shoe

    print(f"The shoe with the highest stock is: {highest_shoe}")


# Main menu to interact with the shoe inventory system
def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Read Shoes Data")
        print("2. Get the Shoes")
        print("3. View Shoes")
        print("4. Restock")
        print("5. Search for Shoes")
        print("6. Value per item")
        print("7. Highest Quantity")
        print("8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Exit.")
            break
        else:
            print("Invalid. Try again.")


# Run the main menu
if __name__ == "__main__":
    main_menu()
