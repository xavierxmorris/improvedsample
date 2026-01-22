"""
Before: Code that could use a different structure.

This module demonstrates code patterns that can be reformatted
to use more modern or idiomatic structures.
"""

import urllib.request
import json


def list_repos(o, p):
    """
    List repositories for an organization.
    
    Problem: Uses old-style function definition and poor parameter names.
    Could use better naming and async/await pattern.
    
    Args:
        o: Organization name.
        p: Number of repos per page.
    
    Returns:
        List of repository data.
    """
    url = f"https://api.github.com/orgs/{o}/repos?per_page={int(p)}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    return data


def calculate_total(items):
    """
    Calculate total from items.
    
    Problem: Uses traditional for loop where reduce could be used.
    """
    total = 0
    for item in items:
        total = total + item['price'] * item['quantity']
    return total


def get_user_info(user):
    """
    Get formatted user info.
    
    Problem: Uses string concatenation instead of f-strings or format.
    """
    name = user['first_name'] + ' ' + user['last_name']
    email = user['email']
    info = 'Name: ' + name + ', Email: ' + email
    return info


def process_numbers(numbers):
    """
    Process a list of numbers.
    
    Problem: Uses traditional loops where map/filter could be cleaner.
    """
    results = []
    for n in numbers:
        if n > 0:
            squared = n * n
            results.append(squared)
    return results


def create_greeting(name, formal):
    """
    Create a greeting message.
    
    Problem: Uses if/else when ternary would be cleaner.
    """
    if formal == True:
        greeting = 'Dear ' + name
    else:
        greeting = 'Hi ' + name
    return greeting


class OldStyleClass:
    """
    An old-style class.
    
    Problem: Doesn't use dataclass, has boilerplate __init__ and __repr__.
    """
    
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return 'OldStyleClass(name=' + self.name + ', age=' + str(self.age) + ', email=' + self.email + ')'
    
    def __eq__(self, other):
        if isinstance(other, OldStyleClass):
            return self.name == other.name and self.age == other.age and self.email == other.email
        return False


def read_file_old_style(filename):
    """
    Read a file.
    
    Problem: Uses open/close without context manager.
    """
    f = open(filename, 'r')
    content = f.read()
    f.close()
    return content


def find_item(items, target):
    """
    Find an item in a list.
    
    Problem: Uses loop when next() with generator would be cleaner.
    """
    found = None
    for item in items:
        if item['id'] == target:
            found = item
            break
    return found


if __name__ == "__main__":
    # Test calculate_total
    items = [
        {'name': 'Widget', 'price': 10, 'quantity': 5},
        {'name': 'Gadget', 'price': 20, 'quantity': 3},
    ]
    print(f"Total: ${calculate_total(items)}")
    
    # Test get_user_info
    user = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john@example.com'}
    print(get_user_info(user))
    
    # Test process_numbers
    numbers = [-2, -1, 0, 1, 2, 3]
    print(f"Processed: {process_numbers(numbers)}")
    
    # Test create_greeting
    print(create_greeting('Alice', True))
    print(create_greeting('Bob', False))
    
    # Test OldStyleClass
    person = OldStyleClass('John', 30, 'john@example.com')
    print(person)
    
    # Test find_item
    products = [{'id': 1, 'name': 'A'}, {'id': 2, 'name': 'B'}]
    print(f"Found: {find_item(products, 2)}")
