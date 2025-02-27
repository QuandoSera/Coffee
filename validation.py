def validate_yes_no(prompt):
    """Validates yes/no inputs and returns the response.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        bool: True for 'yes', False for 'no'
    """
    while True:
        response = input(prompt).lower()
        if response in ('yes', 'y'):
            return True
        elif response in ('no', 'n'):
            return False
        print("Please enter 'yes', 'y', 'no', or 'n'.")


def validate_menu_item(item, menu):
    """Validates if an item exists in the menu using case-insensitive lookup.
    
    Args:
        item (str): The item to validate
        menu (dict): The menu dictionary with items as keys
        
    Returns:
        str: The actual menu item key with proper case if found, None if not found
    """
    item_lower = item.lower()
    if item_lower == 'done':
        return 'done'
        
    # Case-insensitive lookup
    for menu_item in menu:
        if menu_item.lower() == item_lower:
            return menu_item
            
    return None


def validate_positive_number(prompt):
    """Validates that input is a positive number.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        float: A positive number
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def validate_menu_choice(prompt):
    """Validates that input is a positive integer for menu selection.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        int: A positive integer
    """
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def validate_payment_method(prompt):
    """Validates payment method inputs.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        str: Either 'cash' or 'card'
    """
    while True:
        payment_method = input(prompt).lower()
        if payment_method in ("cash", "card"):
            return payment_method
        print("We accept cash or card.")


def validate_name(prompt):
    """Validates name inputs.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        str: A non-empty name string
    """
    while True:
        name = input(prompt)
        if name:
            return name.capitalize()
        print("Please enter your name.")

