"""
Before: Verbose Python code that could be more concise.

This module demonstrates unnecessarily verbose code patterns
that can be simplified without losing clarity.
"""

import math


def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area


def calculate_area_of_circle(radius):
    """Calculate the area of a circle."""
    area = math.pi * (radius ** 2)
    return area


def calculate_area_of_triangle(base, height):
    """Calculate the area of a triangle."""
    area = 0.5 * base * height
    return area


def get_even_numbers(numbers):
    """Get all even numbers from a list."""
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def get_positive_numbers(numbers):
    """Get all positive numbers from a list."""
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers


def convert_to_uppercase(strings):
    """Convert all strings to uppercase."""
    uppercase_strings = []
    for string in strings:
        uppercase_string = string.upper()
        uppercase_strings.append(uppercase_string)
    return uppercase_strings


def check_if_adult(age):
    """Check if a person is an adult."""
    if age >= 18:
        is_adult = True
    else:
        is_adult = False
    return is_adult


def get_status_message(is_active):
    """Get status message based on active state."""
    if is_active == True:
        message = "User is active"
    else:
        message = "User is inactive"
    return message


def read_file_contents(file_path):
    """Read and return file contents."""
    file_handle = open(file_path, 'r')
    contents = file_handle.read()
    file_handle.close()
    return contents


if __name__ == "__main__":
    # Test area calculations
    length_of_rectangle = 10
    width_of_rectangle = 5
    area_of_rectangle = calculate_area_of_rectangle(length_of_rectangle, width_of_rectangle)
    print(f"Area of rectangle: {area_of_rectangle}")

    radius_of_circle = 7
    area_of_circle = calculate_area_of_circle(radius_of_circle)
    print(f"Area of circle: {area_of_circle}")

    base_of_triangle = 8
    height_of_triangle = 6
    area_of_triangle = calculate_area_of_triangle(base_of_triangle, height_of_triangle)
    print(f"Area of triangle: {area_of_triangle}")

    # Test list operations
    my_numbers = [-2, -1, 0, 1, 2, 3, 4, 5]
    even_numbers = get_even_numbers(my_numbers)
    print(f"Even numbers: {even_numbers}")

    positive_numbers = get_positive_numbers(my_numbers)
    print(f"Positive numbers: {positive_numbers}")

    # Test string operations
    my_strings = ["hello", "world", "python"]
    uppercase_strings = convert_to_uppercase(my_strings)
    print(f"Uppercase: {uppercase_strings}")

    # Test boolean operations
    person_age = 21
    is_person_adult = check_if_adult(person_age)
    print(f"Is adult: {is_person_adult}")
