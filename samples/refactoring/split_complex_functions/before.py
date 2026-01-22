"""
Before: Complex function that does too many things.

This module demonstrates functions that violate the Single Responsibility
Principle by performing multiple distinct operations.
"""


def process_data(item: str, price: str) -> None:
    """
    Process product data: cleanse, validate, and display.
    
    Problem: This function does three things:
    1. Cleanses the input data
    2. Validates the data
    3. Formats and prints the data
    
    This makes it hard to test, reuse, and maintain.
    
    Args:
        item: The item name (may have whitespace).
        price: The price as a string (may have whitespace).
    """
    # Cleanse data
    item = item.strip()  # Strip whitespace from item
    price = price.strip()  # Strip whitespace from price
    price = float(price)  # Convert price to a float
    # More cleansing operations could go here

    # Validate data
    if not item:
        raise ValueError("Item name cannot be empty")
    if price < 0:
        raise ValueError("Price cannot be negative")

    # Format and print data
    print(f"Item: {item}")
    print(f"Price: ${price:.2f}")


def process_user_registration(
    first_name: str,
    last_name: str,
    email: str,
    password: str
) -> dict:
    """
    Process a user registration.
    
    Problem: This function handles:
    1. Input validation
    2. Data normalization
    3. Password hashing simulation
    4. User object creation
    
    Args:
        first_name: User's first name.
        last_name: User's last name.
        email: User's email address.
        password: User's password.
    
    Returns:
        Dictionary representing the created user.
    """
    # Validate inputs
    if not first_name or not first_name.strip():
        raise ValueError("First name is required")
    if not last_name or not last_name.strip():
        raise ValueError("Last name is required")
    if not email or "@" not in email:
        raise ValueError("Valid email is required")
    if not password or len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    
    # Normalize data
    first_name = first_name.strip().title()
    last_name = last_name.strip().title()
    email = email.strip().lower()
    
    # Hash password (simplified simulation)
    password_hash = f"hashed_{password[::-1]}"
    
    # Create user object
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": f"{first_name} {last_name}",
        "email": email,
        "password_hash": password_hash,
        "is_active": True
    }
    
    # Log the creation
    print(f"User created: {user['full_name']} ({user['email']})")
    
    return user


def analyze_sales_data(sales: list[dict]) -> None:
    """
    Analyze sales data: calculate totals, find top seller, and print report.
    
    Problem: This function handles:
    1. Calculating total sales
    2. Finding the top-selling product
    3. Calculating average sale
    4. Formatting and printing a report
    
    Args:
        sales: List of sale dictionaries with 'product' and 'amount' keys.
    """
    # Calculate total sales
    total = 0
    for sale in sales:
        total += sale["amount"]
    
    # Find top seller
    top_product = None
    top_amount = 0
    for sale in sales:
        if sale["amount"] > top_amount:
            top_amount = sale["amount"]
            top_product = sale["product"]
    
    # Calculate average
    average = total / len(sales) if sales else 0
    
    # Print report
    print("=" * 40)
    print("SALES REPORT")
    print("=" * 40)
    print(f"Total Sales: ${total:.2f}")
    print(f"Number of Sales: {len(sales)}")
    print(f"Average Sale: ${average:.2f}")
    print(f"Top Product: {top_product} (${top_amount:.2f})")
    print("=" * 40)


if __name__ == "__main__":
    # Test process_data
    print("=== Process Data ===")
    item = "   Apple "
    price = " 1.25"
    process_data(item, price)
    
    # Test user registration
    print("\n=== User Registration ===")
    user = process_user_registration(
        first_name="  john  ",
        last_name="DOE",
        email="  John.Doe@Example.COM  ",
        password="securepassword123"
    )
    
    # Test sales analysis
    print("\n=== Sales Analysis ===")
    sales = [
        {"product": "Widget", "amount": 150.00},
        {"product": "Gadget", "amount": 275.50},
        {"product": "Widget", "amount": 150.00},
        {"product": "Doohickey", "amount": 89.99},
    ]
    analyze_sales_data(sales)
