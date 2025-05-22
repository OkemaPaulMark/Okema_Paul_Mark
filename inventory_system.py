#Assignment 1
# Name: [Okema Paul Mark]
# Simple Inventory Management System

# We have items in the inventory by default first then others can be added later 
#usesd a list of dictionaries to store item details
# Each item has an ID, name, and quantity
inventory = [
    {"id": 1, "name": "Pen", "quantity": 10},
    {"id": 2, "name": "Notebook", "quantity": 5},
    {"id": 3, "name": "Eraser", "quantity": 15}
]

# Display inventory
def display_inventory():
    print("\nCurrent Inventory:")
    print("ID\tName\t\tQuantity")
    for item in inventory:
        print(f"{item['id']}\t{item['name']}\t\t{item['quantity']}")
    print()

# Add a new item
def add_item():
    new_id = int(input("Enter item ID: "))
    name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    inventory.append({"id": new_id, "name": name, "quantity": quantity})
    print("Item added successfully!\n")

# Update item quantity
def update_quantity():
    item_id = int(input("Enter item ID to update: "))
    found = False
    for item in inventory:
        if item["id"] == item_id:
            new_quantity = int(input("Enter new quantity: "))
            item["quantity"] = new_quantity
            print("Quantity updated!\n")
            found = True
            break
    if not found:
        print("Item not found.\n")

# Remove an item
def remove_item():
    item_id = int(input("Enter item ID to remove: "))
    for i in range(len(inventory)):
        if inventory[i]["id"] == item_id:
            del inventory[i]
            print("Item removed!\n")
            return
    print("Item not found.\n")

# Main program loop
def main():
    while True:
        print("Simple Inventory System")
        print("1. Display Inventory")
        print("2. Add Item")
        print("3. Update Quantity")
        print("4. Remove Item")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_quantity()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

# Run the program
main()
