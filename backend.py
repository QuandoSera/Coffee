import json
import re
import validation

def load_menu():
    """Loads the menu data from 'menu.json'."""
    try:
        with open('menu.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("\nError: 'menu.json' not found. Creating a new menu.")
        return {}

def save_menu(menu):
    """Saves the menu data to 'menu.json'."""
    print("\nSaving the menu...")
    try:
        with open('menu.json', 'w', encoding='utf-8') as file:
            json.dump(menu, file, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        print(f"\nError saving menu: {e}")

def add_item(menu):
    """Adds a new item to the menu with validation."""
    new_item = input("\nEnter the name of the new item: ").strip()
    # Updated regex pattern to allow spaces (and now requires at least one alphabetic character)
    if re.match(r"^[a-zA-Z][a-zA-Z0-9\s_]{2,19}$", new_item):  
        try:
            new_price = validation.validate_positive_number(f"\nEnter the price for {new_item}: £")
            menu[new_item] = float(new_price)  # Convert to float for storing in menu
            print(f"\n{new_item} added to the menu successfully!")
        except ValueError:
            print("\nInvalid price. Please enter a positive number.")
    else:
        print("\nInvalid item name. Name must start with a letter and be 3-20 characters long.")

def confirm(message):
    """Asks the user for confirmation."""
    return validation.validate_yes_no(message + " (yes/no): ")

def remove_item(menu):
    """Removes an item from the menu with confirmation."""
    item_to_remove = input("\nEnter the name of the item to remove: ").strip()
    # Case-insensitive lookup
    menu_key = next((k for k in menu.keys() if k.lower() == item_to_remove.lower()), None)
    if menu_key:
        if confirm(f"\nAre you sure you want to remove {menu_key}? "):
            del menu[menu_key]
            print(f"\n{menu_key} removed from the menu.")
        else:
            print("\nRemoval cancelled.")
    else:
        print(f"\n{item_to_remove} not found in the menu.")

def update_price(menu):
    """Updates the price of an item in the menu with validation."""
    item_to_update = input("\nEnter the name of the item to update: ").strip()
    # Case-insensitive lookup
    menu_key = next((k for k in menu.keys() if k.lower() == item_to_update.lower()), None)
    if menu_key:
        try:
            new_price = validation.validate_positive_number(f"\nEnter the new price for {menu_key}: £")
            menu[menu_key] = float(new_price)  # Convert to float for storing in menu
            print(f"\nPrice for {menu_key} updated successfully!")
        except ValueError:
            print("\nInvalid price. Please enter a positive number.")
    else:
        print(f"\n{item_to_update} not found in the menu.")

def display_menu(menu):
    """Displays the menu."""
    print("\nCurrent Menu:\n")
    for item, price in menu.items():
        print(f"\t• {item.capitalize()}: £{price:.2f}")

if __name__ == "__main__":
    menu = load_menu()

    while True:
        print("\nMenu Management Options:\n")
        print("1. Display Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Price")
        print("5. Exit")

        try:
            choice = str(validation.validate_menu_choice("\nEnter your choice (1-5): "))
        except ValueError:
            choice = "0"  # Invalid choice that will trigger the "Invalid choice" message

        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            remove_item(menu)
        elif choice == '4':
            update_price(menu)
        elif choice == '5':
            print("\nExiting...")
            if confirm("\nAre you sure you want to exit? "):
                save_menu(menu)
                print("\nGoodbye!")
                break
            else:
                print("\nContinuing menu management...")
        else:
            print("\nInvalid choice. Please try again.")
