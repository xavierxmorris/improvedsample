"""
After: Code with repeated calculations extracted into functions.

This module demonstrates the refactored version where repeated
calculations are moved into reusable functions.
"""


def calculate_sales(price: float, quantity: int) -> float:
    """
    Calculate sales amount for a product.
    
    Args:
        price: Unit price of the product.
        quantity: Number of units sold.
    
    Returns:
        Total sales amount.
    """
    return price * quantity


def calculate_order_totals() -> None:
    """
    Calculate and display order totals using the helper function.
    """
    total_sales = 0

    total_sales += calculate_sales(price=3, quantity=100)   # Apples
    total_sales += calculate_sales(price=5, quantity=50)    # Oranges
    total_sales += calculate_sales(price=2, quantity=75)    # Bananas
    total_sales += calculate_sales(price=8, quantity=30)    # Grapes

    print(f"Total: ${total_sales}")


def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.
    
    Returns:
        The area of the rectangle.
    """
    return length * width


def calculate_areas() -> None:
    """
    Calculate and display areas of multiple rectangles using the helper function.
    """
    rooms = [
        ("Room 1", 10, 12),
        ("Room 2", 15, 8),
        ("Room 3", 20, 18),
    ]
    
    total_area = 0
    for name, length, width in rooms:
        area = calculate_area(length, width)
        print(f"{name} area: {area} sq ft")
        total_area += area
    
    print(f"Total area: {total_area} sq ft")


def calculate_discounted_price(price: float, discount_percent: float) -> tuple[float, float]:
    """
    Calculate the discount amount and final price.
    
    Args:
        price: Original price.
        discount_percent: Discount percentage (0-100).
    
    Returns:
        Tuple of (discount_amount, final_price).
    """
    discount = price * (discount_percent / 100)
    final_price = price - discount
    return discount, final_price


def calculate_discounts() -> None:
    """
    Calculate discounted prices for products using the helper function.
    """
    items = [
        ("Item 1", 100, 10),
        ("Item 2", 250, 15),
        ("Item 3", 75, 20),
    ]
    
    for name, price, discount_percent in items:
        discount, final = calculate_discounted_price(price, discount_percent)
        print(f"{name}: ${price} - ${discount} = ${final}")


if __name__ == "__main__":
    print("=== Order Totals ===")
    calculate_order_totals()
    
    print("\n=== Room Areas ===")
    calculate_areas()
    
    print("\n=== Discounts ===")
    calculate_discounts()
