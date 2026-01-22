"""
Before: Code with issues that Copilot code review would flag.

This module demonstrates common code quality issues that automated
code review can catch, including:
- Missing error handling for network calls
- Insecure password hashing
- Missing type hints and docstrings
- No logging for debugging
"""

import hashlib
import requests


# =============================================================================
# Issue 1: Network call without error handling
# =============================================================================
# Problems:
# - No timeout: request could hang indefinitely
# - No error handling: exceptions crash the application
# - No logging: can't debug failures
# - No return value: caller doesn't know if it succeeded
# - No type hints: unclear API contract
# - No docstring: poor documentation

def notify_inventory(product_id, quantity):
    requests.post(
        "http://inventory-service/update",
        json={"product_id": product_id, "quantity": quantity}
    )


def process_order(order_id, items):
    # This could fail silently or crash without any indication
    for item in items:
        notify_inventory(item["product_id"], item["quantity"])
    
    # Order marked as confirmed even if inventory notification failed
    return {"order_id": order_id, "status": "CONFIRMED"}


# =============================================================================
# Issue 2: Insecure password hashing using SHA-256
# =============================================================================
# Problems:
# - SHA-256 is too fast, vulnerable to brute-force attacks
# - Manual salt handling is error-prone
# - No iteration/work factor to slow down attacks
# - Should use argon2, bcrypt, or scrypt instead

def get_password_hash(password: str, salt: str) -> str:
    """Hash a password with the given salt using SHA-256.

    Returns the hexadecimal representation of the hashed password.
    """
    return hashlib.sha256((password + salt).encode()).hexdigest()


class User:
    """Represents a user in the order processing system."""

    def __init__(self, username: str, password: str, salt: str):
        """Initialize a User with username, password, and salt.

        The password is hashed and stored for authentication.
        """
        self.username = username
        self.salt = salt
        self.password_hash = get_password_hash(password, self.salt)

    def verify_password(self, password: str) -> bool:
        """Verify a plain-text password against the stored hash."""
        return get_password_hash(password, self.salt) == self.password_hash


# =============================================================================
# Issue 3: Missing input validation
# =============================================================================
# Problems:
# - No validation of order data
# - Could process invalid or malicious input
# - No sanitization before database operations

def create_order(customer_id, items, payment_info):
    # No validation - could accept empty orders, negative quantities, etc.
    order = {
        "customer_id": customer_id,
        "items": items,
        "payment_info": payment_info,  # Storing raw payment info is a security risk
        "total": sum(item["price"] * item["quantity"] for item in items)
    }
    
    # Directly using input without sanitization
    print(f"Created order for customer {customer_id}")
    
    return order


# =============================================================================
# Issue 4: Sensitive data logging
# =============================================================================
# Problems:
# - Logging sensitive payment information
# - Could expose credit card numbers, passwords in logs

def process_payment(order_id, payment_details):
    # BAD: Logging sensitive data
    print(f"Processing payment for order {order_id}: {payment_details}")
    
    # Simulated payment processing
    success = True
    
    if success:
        # BAD: Logging full payment details
        print(f"Payment successful: {payment_details}")
    
    return success


# =============================================================================
# Issue 5: N+1 query pattern
# =============================================================================
# Problems:
# - Makes a separate network call for each item
# - Could be batched into a single call
# - Performance degrades linearly with number of items

def check_inventory_for_order(items):
    """Check inventory for all items in an order."""
    results = []
    
    # N+1 pattern: one call per item instead of batch
    for item in items:
        response = requests.get(
            f"http://inventory-service/check/{item['product_id']}"
        )
        results.append({
            "product_id": item["product_id"],
            "available": response.json().get("available", False)
        })
    
    return results


if __name__ == "__main__":
    # Demo usage (will fail without actual services)
    print("=== Before: Code with issues ===")
    
    # Create a user with insecure password hashing
    user = User("john_doe", "password123", "random_salt")
    print(f"User created: {user.username}")
    print(f"Password hash (SHA-256, insecure): {user.password_hash[:32]}...")
    
    # Create order without validation
    order = create_order(
        customer_id="C123",
        items=[
            {"product_id": "P001", "price": 10.00, "quantity": 2},
            {"product_id": "P002", "price": 25.00, "quantity": 1}
        ],
        payment_info={"card_number": "4111-1111-1111-1111", "cvv": "123"}
    )
    print(f"Order total: ${order['total']}")
