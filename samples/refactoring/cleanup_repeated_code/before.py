"""
Before: Code with repeated calculations.

This module demonstrates code that performs the same calculation
in multiple places, which should be extracted into a function.
"""


def calculate_order_totals() -> None:
    """
    Calculate and display order totals.
    
    Problem: The price * quantity calculation is repeated for each product.
    This violates the DRY (Don't Repeat Yourself) principle.
    """
    total_sales = 0

    # Product 1: Apples
    apple_price = 3
    apples_sold = 100
    total_sales += apple_price * apples_sold

    # Product 2: Oranges
    orange_price = 5
    oranges_sold = 50
    total_sales += orange_price * oranges_sold

    # Product 3: Bananas
    banana_price = 2
    bananas_sold = 75
    total_sales += banana_price * bananas_sold

    # Product 4: Grapes
    grape_price = 8
    grapes_sold = 30
    total_sales += grape_price * grapes_sold

    print(f"Total: ${total_sales}")


def calculate_areas() -> None:
    """
    Calculate and display areas of multiple rectangles.
    
    Problem: The area calculation (length * width) is repeated.
    """
    # Room 1
    room1_length = 10
    room1_width = 12
    room1_area = room1_length * room1_width
    print(f"Room 1 area: {room1_area} sq ft")

    # Room 2
    room2_length = 15
    room2_width = 8
    room2_area = room2_length * room2_width
    print(f"Room 2 area: {room2_area} sq ft")

    # Room 3
    room3_length = 20
    room3_width = 18
    room3_area = room3_length * room3_width
    print(f"Room 3 area: {room3_area} sq ft")

    total_area = room1_area + room2_area + room3_area
    print(f"Total area: {total_area} sq ft")


def calculate_discounts() -> None:
    """
    Calculate discounted prices for products.
    
    Problem: The discount calculation is repeated for each product.
    """
    # Item 1
    item1_price = 100
    item1_discount_percent = 10
    item1_discount = item1_price * (item1_discount_percent / 100)
    item1_final = item1_price - item1_discount
    print(f"Item 1: ${item1_price} - ${item1_discount} = ${item1_final}")

    # Item 2
    item2_price = 250
    item2_discount_percent = 15
    item2_discount = item2_price * (item2_discount_percent / 100)
    item2_final = item2_price - item2_discount
    print(f"Item 2: ${item2_price} - ${item2_discount} = ${item2_final}")

    # Item 3
    item3_price = 75
    item3_discount_percent = 20
    item3_discount = item3_price * (item3_discount_percent / 100)
    item3_final = item3_price - item3_discount
    print(f"Item 3: ${item3_price} - ${item3_discount} = ${item3_final}")


if __name__ == "__main__":
    print("=== Order Totals ===")
    calculate_order_totals()
    
    print("\n=== Room Areas ===")
    calculate_areas()
    
    print("\n=== Discounts ===")
    calculate_discounts()
