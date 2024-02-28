""" This is the newly added backend. It features a menu where we can add items, 
remove items, and update the prices """

import json
import csv
import ast
import datetime
import re # Import the regular expression library

ORDERS_PER_PAGE = 5

def display_order_history(orders, customer_name=None, page_number=1):
    """Displays order history, optionally filtered by customer_name."""
    print("\nCurrent page:", page_number)

    filtered_orders = orders.copy()  # Use the copy() method 

    if customer_name:
        filtered_orders = [order for order in orders if order.get("customer").lower() == customer_name]
        print("Filtered orders:", filtered_orders)

    if not filtered_orders:
        if customer_name:
            print(f"\nNo order history found for {customer_name}.")
        else:
            print("\nNo order history found.")
        return

    start_index = (page_number - 1) * ORDERS_PER_PAGE
    end_index = start_index + ORDERS_PER_PAGE - 1  # Subtract 1 for inclusive end index
    print("Start index:", start_index, "End index:", end_index)
    orders_to_display = filtered_orders[start_index:end_index]
    # print("Orders to display:", orders_to_display)

    show_navigation(len(filtered_orders), page_number)

    # The 'for' loop and its code block should be indented within the function:
    for i, order in enumerate(orders_to_display):
        print(f"\nOrder #{i + 1}\n")
        print("Customer:", order.get("customer", "Unknown"))
        print("Items:", ", ".join(f"{item.title()}: {quantity}" for item, quantity in order["items"].items()))
        print("Total:", order["total"])

        # Format the timestamp nicely
        timestamp_obj = order['timestamp']
        timestamp_str = timestamp_obj.strftime('%d/%m/%Y %H:%M')
        print("Timestamp:", timestamp_str)

        print("-" * 20)

def load_menu():
    """ Loads the menu data from 'menu.json'. """
    try:
        with open('menu.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("\nError: 'menu.json' not found. Creating a new menu.")
        return {}  # Return an empty dictionary if the file is missing

def save_menu(menu):
    """ Saves the menu data to 'menu.json'. """
    print("\nSaving the menu...")
    try:
        with open('menu.json', 'w', encoding='utf-8') as file:
            json.dump(menu, file, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        print(f"\nError saving menu: {e}")

def add_item(menu):
    """ Adds a new item to the menu. """
    new_item = input("\nEnter the name of the new item: ").strip()
    if re.match(r"^[a-zA-Z][a-zA-Z0-9_\s]{2,19}$", new_item):
        while True:  # Keep asking for input
            new_price_str = input(f"\nEnter the price for {new_item}: £")
            try:
                new_price = float(new_price_str)
                if new_price <= 0:
                    raise ValueError("\nPrice must be positive.")  # Extra check
                menu[new_item] = new_price
                print(f"\n{new_item} added to the menu successfully!")
                break  # Exit the loop on successful input
            except ValueError:
                print("\nInvalid price. Please enter a positive number.")
    else:
        print("\nInvalid format. Please use letters, numbers, and underscores (3-20 characters)")

def confirm(message):
    """ Asks the user for confirmation. """
    while True:
        answer = input(message + " (yes/no): ").lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")

def remove_item(menu):
    """ Removes items from the menu. """
    item_to_remove = input("\nEnter the name of the item to remove: ").strip().lower()
    if item_to_remove in (item.lower() for item in menu):
        if confirm(f"\nAre you sure you want to remove {item_to_remove}? "):
            for item in list(menu.keys()):
                if item.lower() == item_to_remove:
                    del menu[item]
                    break
            print(f"\n{item_to_remove} removed from the menu.")
        else:
            print("\nRemoval canceled.")
    else:
        print(f"\n{item_to_remove} not found in the menu.")

def update_price(menu):
    """ Updates the price of items on the menu. """
    item_to_update = input("\nEnter the name of the item to update: ").strip().lower()

    found = False
    for item in menu.keys():
        if item.lower() == item_to_update:
            found = True
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
            break  # Exit the 'for' loop since the item was found

    if not found:
        print(f"\n{item_to_update} not found in the menu.")

def display_menu(menu):
    """ Displays the menu. """
    print("\nCurrent Menu:\n")
    for item, price in menu.items():
        print(f"\t• {item.capitalize()}: £{price:.2f}")

def load_orders():
    """Loads order data from 'orders.csv'."""
    try:
        with open('orders.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            orders = list(reader)

            for order in orders:
                if isinstance(order['items'], str): 
                    order['items'] = ast.literal_eval(order['items']) 

                # Convert the timestamp string into a datetime object
                date_str = order['timestamp']
                date_obj = datetime.datetime.strptime(date_str, '%d/%m/%Y %H:%M')
                order['timestamp'] = date_obj 

            # print("Orders loaded:", orders)  
            return orders
    except FileNotFoundError:
        return []

def show_navigation(total_orders, current_page):
    max_page = (total_orders // ORDERS_PER_PAGE) + 1  # Existing calculation

    # Adjust only if needed:
    if total_orders <= ORDERS_PER_PAGE: 
        max_page = 1  

    if current_page > 1:
        print("1. Previous Page")
    if current_page < max_page:
        print("2. Next Page")
    print("3. Exit to Main Menu")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == '1' and current_page > 1:
            return current_page - 1
        elif choice == '2' and current_page < max_page:
            return current_page + 1
        elif choice == '3':
            return None
        else:
            print("\nInvalid choice. Please try again.")

def view_order_history():
    all_orders = load_orders()  # Load the original orders
    orders = all_orders.copy()  # Create a copy

    customer_name = input("\nEnter a customer's name (optional): ").lower()
    if customer_name:  # Only if filtering is requested
        display_order_history(orders, customer_name=customer_name, page_number=1) 
    else: 
        display_order_history(all_orders, page_number=1) # Use the unfiltered list

        print("Total Orders:", len(all_orders))
        print("Filtered Orders (if any):", len(orders))

# Main logic
if __name__ == "__main__":
    menu = load_menu()

    while True:
        print("\nManagement Menu:\n")
        print("1. Display Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Update Price")
        print("5. View Order History")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            display_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            remove_item(menu)
        elif choice == '4':
            update_price(menu)
        elif choice == '5':
            view_order_history()
        elif choice == '6':
            print("\nExiting...")
            if confirm("\nAre you sure you want to exit? "):
                save_menu(menu)
                print("\nGoodbye!")
                break
            else:
                print("\nContinuing menu management...")
        else:
            print("\nInvalid choice. Please try again.")
