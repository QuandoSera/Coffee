import json
import re

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
        while True:
            new_price_str = input(f"\nEnter the price for {new_item}: £")
            try:
                new_price = float(new_price_str)
                if new_price <= 0:
                    raise ValueError("\nPrice must be positive.")
                menu[new_item] = new_price
                print(f"\n{new_item} added to the menu successfully!")
                break
            except ValueError:
                print("\nInvalid price. Please enter a positive number.")
    else:
        print("\nInvalid format. Please use letters, numbers, spaces, and underscores (3-20 characters)")

def confirm(message):
    """Asks the user for confirmation."""
    while True:
        answer = input(message + " (yes/no): ").lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")

def remove_item(menu):
    """Removes an item from the menu with confirmation."""
    item_to_remove = input("\nEnter the name of the item to remove: ").strip().lower()
    if item_to_remove in menu:
        if confirm(f"\nAre you sure you want to remove {item_to_remove}? "):
            del menu[item_to_remove]
            print(f"\n{item_to_remove} removed from the menu.")
        else:
            print("\nRemoval cancelled.")
    else:
        print(f"\n{item_to_remove} not found in the menu.")

def update_price(menu):
    """Updates the price of an item in the menu with validation."""
    item_to_update = input("\nEnter the name of the item to update: ").strip().lower()
    if item_to_update in menu:
        while True:
            new_price_str = input(f"\nEnter the new price for {item_to_update}: £")
            try:
                new_price = float(new_price_str)
                if new_price <= 0:
                    raise ValueError("\nPrice must be positive.")
                menu[item_to_update] = new_price
                print(f"\nPrice for {item_to_update} updated successfully!")
                break
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
            print("\nExiting...")
            if confirm("\nAre you sure you want to exit? "):
                save_menu(menu)
                print("\nGoodbye!")
                break
            else:
                print("\nContinuing menu management...")
        else:
            print("\nInvalid choice. Please try again.")