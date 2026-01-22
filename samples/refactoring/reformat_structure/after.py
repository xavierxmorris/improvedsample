"""
After: Code reformatted to use modern Python structures.

This module demonstrates the same functionality using more
modern and idiomatic Python patterns.
"""

import urllib.request
import json
from dataclasses import dataclass
from functools import reduce
from typing import Optional


def list_repositories(organization: str, per_page: int) -> list[dict]:
    """
    List repositories for an organization.
    
    Uses descriptive parameter names and type hints.
    
    Args:
        organization: The GitHub organization name.
        per_page: Number of repositories to fetch per page.
    
    Returns:
        List of repository data dictionaries.
    """
    url = f"https://api.github.com/orgs/{organization}/repos?per_page={per_page}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def calculate_total(items: list[dict]) -> float:
    """
    Calculate total from items using reduce.
    
    Args:
        items: List of items with 'price' and 'quantity' keys.
    
    Returns:
        The total value.
    """
    return reduce(
        lambda total, item: total + item['price'] * item['quantity'],
        items,
        0
    )


# Alternative: sum with generator expression (often preferred)
def calculate_total_alt(items: list[dict]) -> float:
    """Calculate total using sum with generator expression."""
    return sum(item['price'] * item['quantity'] for item in items)


def get_user_info(user: dict) -> str:
    """
    Get formatted user info using f-strings.
    
    Args:
        user: User dictionary with 'first_name', 'last_name', 'email' keys.
    
    Returns:
        Formatted user information string.
    """
    name = f"{user['first_name']} {user['last_name']}"
    return f"Name: {name}, Email: {user['email']}"


def process_numbers(numbers: list[int]) -> list[int]:
    """
    Process a list of numbers using list comprehension.
    
    Args:
        numbers: List of numbers to process.
    
    Returns:
        List of squared positive numbers.
    """
    return [n ** 2 for n in numbers if n > 0]


# Alternative: using map and filter
def process_numbers_functional(numbers: list[int]) -> list[int]:
    """Process numbers using functional approach."""
    return list(map(lambda n: n ** 2, filter(lambda n: n > 0, numbers)))


def create_greeting(name: str, formal: bool = False) -> str:
    """
    Create a greeting message using ternary expression.
    
    Args:
        name: The person's name.
        formal: Whether to use formal greeting.
    
    Returns:
        The greeting message.
    """
    return f"Dear {name}" if formal else f"Hi {name}"


@dataclass
class Person:
    """
    A modern dataclass replacing boilerplate class.
    
    Dataclass automatically provides __init__, __repr__, __eq__, and more.
    """
    name: str
    age: int
    email: str


def read_file(filename: str) -> str:
    """
    Read a file using context manager.
    
    Args:
        filename: Path to the file to read.
    
    Returns:
        The file contents.
    """
    with open(filename, 'r') as f:
        return f.read()


def find_item(items: list[dict], target: int) -> Optional[dict]:
    """
    Find an item in a list using next() with generator.
    
    Args:
        items: List of items to search.
        target: The ID to search for.
    
    Returns:
        The found item, or None if not found.
    """
    return next((item for item in items if item['id'] == target), None)


if __name__ == "__main__":
    # Test calculate_total
    items = [
        {'name': 'Widget', 'price': 10, 'quantity': 5},
        {'name': 'Gadget', 'price': 20, 'quantity': 3},
    ]
    print(f"Total: ${calculate_total(items)}")
    print(f"Total (alt): ${calculate_total_alt(items)}")
    
    # Test get_user_info
    user = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'}
    print(get_user_info(user))
    
    # Test process_numbers
    numbers = [-2, -1, 0, 1, 2, 3]
    print(f"Processed: {process_numbers(numbers)}")
    print(f"Processed (functional): {process_numbers_functional(numbers)}")
    
    # Test create_greeting
    print(create_greeting('Alice', formal=True))
    print(create_greeting('Bob'))
    
    # Test Person dataclass
    person = Person('John', 30, 'john@example.com')
    print(person)
    print(f"Equality test: {person == Person('John', 30, 'john@example.com')}")
    
    # Test find_item
    products = [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]
    print(f"Found: {find_item(products, 2)}")
    print(f"Not found: {find_item(products, 99)}")
