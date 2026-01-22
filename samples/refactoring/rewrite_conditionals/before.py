"""
Before: Conditional code that could be more readable.

This module demonstrates various conditional patterns that can
be rewritten for better readability using pattern matching
and other techniques.
"""

from typing import Optional


def get_animal_sound(animal: Optional[str]) -> str:
    """
    Get the sound an animal makes.
    
    Problem: Long chain of if/elif statements. In Python 3.10+,
    this could use structural pattern matching (match/case).
    
    Args:
        animal: The name of the animal, or None.
    
    Returns:
        The sound the animal makes, or "Unknown".
    """
    if animal is None:
        print("Oops! A null animal?")
        return "Unknown"
    elif animal.lower() == "dog":
        return "Bark"
    elif animal.lower() == "cat":
        return "Meow"
    elif animal.lower() == "bird":
        return "Tweet"
    elif animal.lower() == "cow":
        return "Moo"
    elif animal.lower() == "duck":
        return "Quack"
    else:
        return "Unknown"


def get_http_status_message(status_code: int) -> str:
    """
    Get a message for an HTTP status code.
    
    Problem: Multiple elif statements checking ranges.
    Could use match/case with guards.
    
    Args:
        status_code: The HTTP status code.
    
    Returns:
        A human-readable status message.
    """
    if status_code >= 200 and status_code < 300:
        return "Success"
    elif status_code >= 300 and status_code < 400:
        return "Redirect"
    elif status_code >= 400 and status_code < 500:
        return "Client Error"
    elif status_code >= 500 and status_code < 600:
        return "Server Error"
    elif status_code >= 100 and status_code < 200:
        return "Informational"
    else:
        return "Unknown Status"


def calculate_shipping(weight: float, destination: str) -> float:
    """
    Calculate shipping cost based on weight and destination.
    
    Problem: Nested conditionals make this hard to follow.
    
    Args:
        weight: Package weight in pounds.
        destination: Shipping destination ("domestic", "international").
    
    Returns:
        Shipping cost in dollars.
    """
    if destination == "domestic":
        if weight <= 1:
            return 5.00
        elif weight <= 5:
            return 10.00
        elif weight <= 20:
            return 20.00
        else:
            return 50.00
    elif destination == "international":
        if weight <= 1:
            return 15.00
        elif weight <= 5:
            return 30.00
        elif weight <= 20:
            return 60.00
        else:
            return 150.00
    else:
        raise ValueError(f"Unknown destination: {destination}")


def get_grade(score: int) -> str:
    """
    Convert a numeric score to a letter grade.
    
    Problem: Multiple range checks with elif.
    
    Args:
        score: The numeric score (0-100).
    
    Returns:
        The letter grade.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def process_command(command: str, args: list) -> str:
    """
    Process a command with arguments.
    
    Problem: Multiple string comparisons with if/elif.
    Perfect candidate for match/case.
    
    Args:
        command: The command name.
        args: List of command arguments.
    
    Returns:
        The command result.
    """
    if command == "add":
        if len(args) >= 2:
            return str(float(args[0]) + float(args[1]))
        else:
            return "Error: add requires 2 arguments"
    elif command == "subtract":
        if len(args) >= 2:
            return str(float(args[0]) - float(args[1]))
        else:
            return "Error: subtract requires 2 arguments"
    elif command == "multiply":
        if len(args) >= 2:
            return str(float(args[0]) * float(args[1]))
        else:
            return "Error: multiply requires 2 arguments"
    elif command == "divide":
        if len(args) >= 2:
            if float(args[1]) != 0:
                return str(float(args[0]) / float(args[1]))
            else:
                return "Error: division by zero"
        else:
            return "Error: divide requires 2 arguments"
    elif command == "help":
        return "Available commands: add, subtract, multiply, divide, help"
    else:
        return f"Unknown command: {command}"


if __name__ == "__main__":
    # Test animal sounds
    print("=== Animal Sounds ===")
    for animal in ["Dog", "CAT", "Bird", None, "Lion"]:
        print(f"{animal}: {get_animal_sound(animal)}")
    
    # Test HTTP status
    print("\n=== HTTP Status ===")
    for code in [200, 301, 404, 500, 999]:
        print(f"{code}: {get_http_status_message(code)}")
    
    # Test shipping
    print("\n=== Shipping Costs ===")
    for weight in [0.5, 3, 15, 30]:
        domestic = calculate_shipping(weight, "domestic")
        intl = calculate_shipping(weight, "international")
        print(f"{weight} lbs: domestic=${domestic}, international=${intl}")
    
    # Test grades
    print("\n=== Grades ===")
    for score in [95, 85, 75, 65, 55]:
        print(f"{score}: {get_grade(score)}")
    
    # Test commands
    print("\n=== Commands ===")
    print(process_command("add", ["5", "3"]))
    print(process_command("divide", ["10", "2"]))
    print(process_command("help", []))
    print(process_command("unknown", []))
