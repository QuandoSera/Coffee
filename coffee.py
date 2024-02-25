""" This small python project simulates a coffee shop ordering experience.
It features a menu with prices, order customization, input validation, 
and calculates the total cost of an order. """

# Menu and prices
menu = {
    "black coffee": 3,
    "espresso": 2,
    "latte": 4,
    "cappuccino": 4,
    "cortado": 3,
    "flat white": 3
}

# Welcome message
print("Hello, welcome to Jitters's Coffee Shop ☕️")

# Get the customer's name
name = input("Let's start with introductions! What's your name? ")
print(f"\nNice to meet you, {name.capitalize()}! Let's see what we can get you.")

# Display the menu with formatting
print("\nHere's what we're serving today:")
for item, price in menu.items():
    print(f"\t• {item.capitalize()}: £{price:.2f}")

# Order taking loop
order_items = []  # Store the customer's order
while True:
    order = input("\nWhat would you like to order? (Type 'menu' to see options) ").title()
    if order == "Menu":
        print("\nNo problem! Here's the menu again:")
        for item, price in menu.items():
            print(f"\t• {item.capitalize()}: £{price:.2f}")
        continue

    while True:
        if order.lower() not in menu:
            print(f"Sorry, it looks like we don't have '{order}'.")
            print("Would you like to try something else from the menu?")
            break

        quantity_str = input(f"\nGreat choice! How many {order.lower()}'s would you like? ")
        if quantity_str.isdigit() and int(quantity_str) > 0:
            quantity = int(quantity_str)
            order_items.append((order, quantity))
            break
        else:
            print("\nPlease enter a valid quantity.")

    another_order = input("\nWould you like to add anything else to your order (yes/no)? ").lower()
    if another_order not in ("yes", "no"):
        print("\nSorry, I didn't quite catch that. Could you please answer with 'yes' or 'no'?")
    elif another_order == "no":
        break

# Order Summary
print(f"\nGreat choices, {name.capitalize()}! For your order, I have:")
for i, (item, quantity) in enumerate(order_items):
    print(f"\t{i + 1}. {quantity} {item}{'s' if quantity > 1 else ''}")

# Calculate the total price
TOTAL_PRICE = 0.0
for item, quantity in order_items:
    price = menu.get(item.lower())
    if price is not None:
        TOTAL_PRICE += price * quantity
print(f"\nYour total comes to: £{TOTAL_PRICE:.2f}")

# Payment Handling
PAYMENT_METHOD = ""
while PAYMENT_METHOD.lower() not in ("cash", "card"):
    PAYMENT_METHOD = input("\nHow would you like to pay today (cash/card)? ").lower()
    if PAYMENT_METHOD.lower() not in ("cash", "card"):
        print("\nFor your convenience, we accept cash or card.")

# Personalized Thank You
if PAYMENT_METHOD == "cash":
    print(f"\nThank you for paying with cash, {name.capitalize()}!")
    print("We'll have your order ready for you in just a few moments.")
elif PAYMENT_METHOD == "card":
    print(f"\nThank you, {name.capitalize()}.")
    print("Please insert your card, and we'll process your payment right away.")

# Final Message with Order Details
print(f"\nJust a reminder {name.capitalize()}, your order includes:")
for i, (item, quantity) in enumerate(order_items):
    print(f"\t{i + 1}. {quantity} {item}{'s' if quantity > 1 else ''}")

print(f"""\nThanks again for choosing Jitters's Coffee Shop {name.capitalize()}!
We hope you enjoy your drinks!""")
