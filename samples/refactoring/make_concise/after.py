"""
After: Concise Python code using idiomatic patterns.

This module demonstrates the same functionality as before.py
but written in a more Pythonic and concise manner.
"""

import math


def calculate_rectangle_area(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    return length * width


def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return math.pi * radius ** 2


def calculate_triangle_area(base: float, height: float) -> float:
    """Calculate the area of a triangle."""
    return 0.5 * base * height


def get_even_numbers(numbers: list[int]) -> list[int]:
    """Get all even numbers from a list."""
    return [n for n in numbers if n % 2 == 0]


def get_positive_numbers(numbers: list[int]) -> list[int]:
    """Get all positive numbers from a list."""
    return [n for n in numbers if n > 0]


def convert_to_uppercase(strings: list[str]) -> list[str]:
    """Convert all strings to uppercase."""
    return [s.upper() for s in strings]


def is_adult(age: int) -> bool:
    """Check if a person is an adult."""
    return age >= 18


def get_status_message(is_active: bool) -> str:
    """Get status message based on active state."""
    return "User is active" if is_active else "User is inactive"


def read_file_contents(file_path: str) -> str:
    """Read and return file contents."""
    with open(file_path, 'r') as f:
        return f.read()


if __name__ == "__main__":
    # Test area calculations - direct inline usage
    print(f"Area of rectangle: {calculate_rectangle_area(10, 5)}")
    print(f"Area of circle: {calculate_circle_area(7)}")
    print(f"Area of triangle: {calculate_triangle_area(8, 6)}")

    # Test list operations
    numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
    print(f"Even numbers: {get_even_numbers(numbers)}")
    print(f"Positive numbers: {get_positive_numbers(numbers)}")

    # Test string operations
    strings = ["hello", "world", "python"]
    print(f"Uppercase: {convert_to_uppercase(strings)}")

    # Test boolean operations
    print(f"Is adult: {is_adult(21)}")
