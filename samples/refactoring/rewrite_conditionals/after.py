"""
After: Conditional code rewritten for better readability.

This module demonstrates the same functionality using Python 3.10+
pattern matching (match/case) and other improved patterns.
"""

from typing import Optional


def get_animal_sound(animal: Optional[str]) -> str:
    """
    Get the sound an animal makes using pattern matching.
    
    Args:
        animal: The name of the animal, or None.
    
    Returns:
        The sound the animal makes, or "Unknown".
    """
    match animal:
        case None:
            print("Oops! A null animal?")
            return "Unknown"
        case str(a) if a.lower() == "dog":
            return "Bark"
        case str(a) if a.lower() == "cat":
            return "Meow"
        case str(a) if a.lower() == "bird":
            return "Tweet"
        case str(a) if a.lower() == "cow":
            return "Moo"
        case str(a) if a.lower() == "duck":
            return "Quack"
        case _:
            return "Unknown"


# Alternative: Dictionary-based approach (often cleaner than match for simple mappings)
ANIMAL_SOUNDS = {
    "dog": "Bark",
    "cat": "Meow",
    "bird": "Tweet",
    "cow": "Moo",
    "duck": "Quack",
}


def get_animal_sound_dict(animal: Optional[str]) -> str:
    """
    Get the sound an animal makes using dictionary lookup.
    
    This is often the cleanest approach for simple value mappings.
    """
    if animal is None:
        print("Oops! A null animal?")
        return "Unknown"
    return ANIMAL_SOUNDS.get(animal.lower(), "Unknown")


def get_http_status_message(status_code: int) -> str:
    """
    Get a message for an HTTP status code using pattern matching with guards.
    
    Args:
        status_code: The HTTP status code.
    
    Returns:
        A human-readable status message.
    """
    match status_code:
        case code if 100 <= code < 200:
            return "Informational"
        case code if 200 <= code < 300:
            return "Success"
        case code if 300 <= code < 400:
            return "Redirect"
        case code if 400 <= code < 500:
            return "Client Error"
        case code if 500 <= code < 600:
            return "Server Error"
        case _:
            return "Unknown Status"


# Shipping rates as data instead of nested conditionals
SHIPPING_RATES = {
    "domestic": [(1, 5.00), (5, 10.00), (20, 20.00), (float('inf'), 50.00)],
    "international": [(1, 15.00), (5, 30.00), (20, 60.00), (float('inf'), 150.00)],
}


def calculate_shipping(weight: float, destination: str) -> float:
    """
    Calculate shipping cost using data-driven approach.
    
    Args:
        weight: Package weight in pounds.
        destination: Shipping destination ("domestic", "international").
    
    Returns:
        Shipping cost in dollars.
    
    Raises:
        ValueError: If destination is unknown.
    """
    if destination not in SHIPPING_RATES:
        raise ValueError(f"Unknown destination: {destination}")
    
    for max_weight, cost in SHIPPING_RATES[destination]:
        if weight <= max_weight:
            return cost
    
    # Should never reach here due to infinity in rates
    return SHIPPING_RATES[destination][-1][1]


# Grade boundaries as data
GRADE_BOUNDARIES = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]


def get_grade(score: int) -> str:
    """
    Convert a numeric score to a letter grade using data-driven approach.
    
    Args:
        score: The numeric score (0-100).
    
    Returns:
        The letter grade.
    """
    for min_score, grade in GRADE_BOUNDARIES:
        if score >= min_score:
            return grade
    return "F"


def process_command(command: str, args: list) -> str:
    """
    Process a command with arguments using pattern matching.
    
    Args:
        command: The command name.
        args: List of command arguments.
    
    Returns:
        The command result.
    """
    match (command, args):
        case ("add", [a, b, *_]):
            return str(float(a) + float(b))
        case ("subtract", [a, b, *_]):
            return str(float(a) - float(b))
        case ("multiply", [a, b, *_]):
            return str(float(a) * float(b))
        case ("divide", [a, b, *_]) if float(b) != 0:
            return str(float(a) / float(b))
        case ("divide", [_, b, *_]) if float(b) == 0:
            return "Error: division by zero"
        case ("add" | "subtract" | "multiply" | "divide", _):
            return f"Error: {command} requires 2 arguments"
        case ("help", _):
            return "Available commands: add, subtract, multiply, divide, help"
        case _:
            return f"Unknown command: {command}"


if __name__ == "__main__":
    # Test animal sounds
    print("=== Animal Sounds ===")
    for animal in ["Dog", "CAT", "Bird", None, "Lion"]:
        print(f"{animal}: {get_animal_sound(animal)}")
    
    print("\n=== Animal Sounds (Dict) ===")
    for animal in ["Dog", "CAT", "Bird", None, "Lion"]:
        print(f"{animal}: {get_animal_sound_dict(animal)}")
    
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
