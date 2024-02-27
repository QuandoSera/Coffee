import json

def load_menu(filename="menu.json"):
    with open(filename, 'r') as file:
        return json.load(file)

def save_menu(menu, filename="menu.json"):
    with open(filename, 'w') as file:
        json.dump(menu, file, indent=4)

def add_item(menu):
    new_item = input("\nEnter the name of the new item: ")
    new_price_str = input(f"\nEnter the price for {new_item}: £")
    try:
        new_price = float(new_price_str)
        menu[new_item] = new_price
        print(f"\n{new_item} added to the menu successfully!")
    except ValueError:
        print("\nInvalid price. Please enter a number.")

def remove_item(menu):
    item_to_remove = input("\nEnter the name of the item to remove: ")
    if item_to_remove in menu:
        del menu[item_to_remove]
        print(f"\n{item_to_remove} removed from the menu.")
    else:
        print(f"\n{item_to_remove} not found in the menu.")

def update_price(menu):
    item_to_update = input("\nEnter the name of the item to update: ")
    if item_to_update in menu:
        new_price_str = input(f"\nEnter the new price for {item_to_update}: £")
        try:
            new_price = float(new_price_str)
            menu[item_to_update] = new_price
            print(f"Price for {item_to_update} updated successfully!")
        except ValueError:
            print("\nInvalid price. Please enter a number.")
    else:
        print(f"\n{item_to_update} not found in the menu.")

def display_menu(menu):
    print("Current Menu:")
    for item, price in menu.items():
        print(f"\t• {item.capitalize()}: £{price:.2f}")

# Main logic
if __name__ == "__main__":
    menu = load_menu()

    while True:
        print("\nMenu Management Options:\n")
        print("1. Display Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Price")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            remove_item(menu)
        elif choice == '4':
            update_price(menu)
        elif choice == '5':
            save_menu(menu)
            print("\nMenu updates saved. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
