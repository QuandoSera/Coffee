import json
import validation

def display_menu(menu):
    """Displays the coffee shop menu."""
    print("\nHere's what we're serving today:")
    for item, price in menu.items():
        print(f"\t• {item.capitalize()}: £{price:.2f}")

def get_customer_name():
    """Gets the customer's name with input validation."""
    return validation.validate_name("Let's start with introductions! What's your name? ")

def take_order(menu):
    """Takes the customer's order with input validation."""
    order_items = []  # Initialize as an empty list
    while True:
        display_menu(menu)
        while True:
            order = input("\nWhat would you like to order? (or type 'done'): ").lower()
            if order == 'done':
                return order_items
            valid_item = validation.validate_menu_item(order, menu)
            if valid_item:
                order = valid_item  # Use the correctly-cased key from the menu
                break
            print(f"Sorry, we don't have '{order}'. Please choose from the menu.")
        
        # Ask for quantity
        quantity = validation.validate_positive_number(f"How many {order}s would you like? ")
        
        order_items.append((order, quantity))
        
        if not validation.validate_yes_no("Anything else? (yes/no): "):
            break
    return order_items

def calculate_total(order_items, menu):
    """Calculates the total cost of the order."""
    total = 0
    for item, quantity in order_items:
        price = menu.get(item)
        if price is not None:
            total += price * quantity
    return total

def print_order_summary(order_items, menu):
    """Prints a summary of the order."""
    if not order_items:
        print("\nNo items were ordered.")
        return

    print("\nYour order summary:")
    for i, (item, quantity) in enumerate(order_items):
        item_price = menu[item]
        item_total = item_price * quantity
        print(f"{i + 1}. {int(quantity)} {item}{'s' if quantity > 1 else ''}: £{item_total:.2f}")

def handle_payment(total, name):
    """Handles payment with input validation."""
    while True:
        payment_method = input(f"\nYour total is £{total:.2f}. How would you like to pay (cash/card)? ").lower()
        if payment_method in ("cash", "card"):
            break
        print("We accept cash or card.")

    if payment_method == "cash":
        print(f"\nThank you for paying with cash, {name}!")
    else:  # card
        print(f"\nThank you, {name}. Please insert your card to process the payment.")  # Simulated card payment

def thank_you_message(name):
    print(f"\nThank you for choosing Jitters' Coffee Shop, {name}!")
    print("We hope you enjoy your drinks!")

def main():
    """Main function to run the coffee shop simulation."""
    try:
        with open('menu.json', 'r', encoding='utf-8') as file:
            menu = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading menu: {e}")
        return

    name = get_customer_name()
    print(f"\nWelcome, {name}!")

    order = take_order(menu)
    if not order:
        print("\nNo order was placed.")
        return

    print_order_summary(order, menu)

    total = calculate_total(order, menu)
    print(f"\nYour total is: £{total:.2f}")

    handle_payment(total, name)
    thank_you_message(name)

if __name__ == "__main__":
    main()