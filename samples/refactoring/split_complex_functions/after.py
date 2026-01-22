"""
After: Complex functions split into smaller, focused units.

This module demonstrates the same functionality split into
single-responsibility functions that are easier to test and reuse.
"""

from dataclasses import dataclass
from typing import Optional


# ============================================================
# Product Data Processing (split into 3 functions)
# ============================================================

def cleanse_product_data(item: str, price: str) -> tuple[str, float]:
    """
    Cleanse product data by stripping whitespace and converting types.
    
    Args:
        item: The item name (may have whitespace).
        price: The price as a string (may have whitespace).
    
    Returns:
        Tuple of (cleaned_item, cleaned_price).
    """
    item = item.strip()
    price_float = float(price.strip())
    return item, price_float


def validate_product_data(item: str, price: float) -> None:
    """
    Validate product data.
    
    Args:
        item: The item name.
        price: The price as a float.
    
    Raises:
        ValueError: If item is empty or price is negative.
    """
    if not item:
        raise ValueError("Item name cannot be empty")
    if price < 0:
        raise ValueError("Price cannot be negative")


def display_product_data(item: str, price: float) -> None:
    """
    Display product data in a formatted way.
    
    Args:
        item: The item name.
        price: The price.
    """
    print(f"Item: {item}")
    print(f"Price: ${price:.2f}")


def process_data(item: str, price: str) -> None:
    """
    Process product data using the three helper functions.
    
    Args:
        item: The item name (may have whitespace).
        price: The price as a string (may have whitespace).
    """
    item, price_float = cleanse_product_data(item, price)
    validate_product_data(item, price_float)
    display_product_data(item, price_float)


# ============================================================
# User Registration (split into focused functions)
# ============================================================

@dataclass
class User:
    """Represents a registered user."""
    first_name: str
    last_name: str
    email: str
    password_hash: str
    is_active: bool = True
    
    @property
    def full_name(self) -> str:
        """Get the user's full name."""
        return f"{self.first_name} {self.last_name}"


def validate_registration_input(
    first_name: str,
    last_name: str,
    email: str,
    password: str
) -> None:
    """
    Validate user registration inputs.
    
    Raises:
        ValueError: If any input is invalid.
    """
    if not first_name or not first_name.strip():
        raise ValueError("First name is required")
    if not last_name or not last_name.strip():
        raise ValueError("Last name is required")
    if not email or "@" not in email:
        raise ValueError("Valid email is required")
    if not password or len(password) < 8:
        raise ValueError("Password must be at least 8 characters")


def normalize_user_data(first_name: str, last_name: str, email: str) -> tuple[str, str, str]:
    """
    Normalize user data (strip whitespace, apply casing rules).
    
    Returns:
        Tuple of (normalized_first, normalized_last, normalized_email).
    """
    return (
        first_name.strip().title(),
        last_name.strip().title(),
        email.strip().lower()
    )


def hash_password(password: str) -> str:
    """
    Hash a password (simplified simulation).
    
    Args:
        password: The plain text password.
    
    Returns:
        The hashed password.
    """
    return f"hashed_{password[::-1]}"


def create_user(first_name: str, last_name: str, email: str, password_hash: str) -> User:
    """
    Create a User object.
    
    Returns:
        The created User instance.
    """
    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=password_hash
    )


def process_user_registration(
    first_name: str,
    last_name: str,
    email: str,
    password: str
) -> User:
    """
    Process a user registration using the helper functions.
    """
    validate_registration_input(first_name, last_name, email, password)
    first_name, last_name, email = normalize_user_data(first_name, last_name, email)
    password_hash = hash_password(password)
    user = create_user(first_name, last_name, email, password_hash)
    print(f"User created: {user.full_name} ({user.email})")
    return user


# ============================================================
# Sales Analysis (split into focused functions)
# ============================================================

@dataclass
class SalesReport:
    """Represents a sales analysis report."""
    total: float
    count: int
    average: float
    top_product: Optional[str]
    top_amount: float


def calculate_total_sales(sales: list[dict]) -> float:
    """Calculate the total of all sales."""
    return sum(sale["amount"] for sale in sales)


def find_top_seller(sales: list[dict]) -> tuple[Optional[str], float]:
    """Find the top-selling product."""
    if not sales:
        return None, 0.0
    top_sale = max(sales, key=lambda s: s["amount"])
    return top_sale["product"], top_sale["amount"]


def calculate_average_sale(total: float, count: int) -> float:
    """Calculate the average sale amount."""
    return total / count if count > 0 else 0.0


def generate_sales_report(sales: list[dict]) -> SalesReport:
    """Generate a sales report from sales data."""
    total = calculate_total_sales(sales)
    top_product, top_amount = find_top_seller(sales)
    average = calculate_average_sale(total, len(sales))
    
    return SalesReport(
        total=total,
        count=len(sales),
        average=average,
        top_product=top_product,
        top_amount=top_amount
    )


def print_sales_report(report: SalesReport) -> None:
    """Print a formatted sales report."""
    print("=" * 40)
    print("SALES REPORT")
    print("=" * 40)
    print(f"Total Sales: ${report.total:.2f}")
    print(f"Number of Sales: {report.count}")
    print(f"Average Sale: ${report.average:.2f}")
    print(f"Top Product: {report.top_product} (${report.top_amount:.2f})")
    print("=" * 40)


def analyze_sales_data(sales: list[dict]) -> None:
    """Analyze sales data and print a report."""
    report = generate_sales_report(sales)
    print_sales_report(report)


if __name__ == "__main__":
    # Test process_data
    print("=== Process Data ===")
    process_data("   Apple ", " 1.25")
    
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
