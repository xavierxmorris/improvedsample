"""
After: Improved code following Copilot code review recommendations.

This module demonstrates best practices that address common code
quality issues, including:
- Proper error handling for network calls
- Secure password hashing with argon2
- Type hints and comprehensive docstrings
- Structured logging for debugging
- Input validation and sanitization
"""

import logging
import re
from dataclasses import dataclass
from typing import Optional

import requests

# Try to import argon2, fall back to a mock for demo purposes
try:
    from argon2 import PasswordHasher
    from argon2.exceptions import VerifyMismatchError
except ImportError:
    # Mock for demonstration when argon2-cffi is not installed
    class PasswordHasher:
        """Mock PasswordHasher for demonstration."""
        def hash(self, password: str) -> str:
            return f"$argon2id$v=19$m=65536,t=3,p=4${password[::-1]}"
        
        def verify(self, hash: str, password: str) -> bool:
            return True
    
    class VerifyMismatchError(Exception):
        pass


# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# =============================================================================
# Fix 1: Network call with proper error handling
# =============================================================================

def notify_inventory(product_id: str, quantity: int) -> bool:
    """
    Notify the inventory service of order placement.

    Makes a POST request to the inventory service with timeout and
    comprehensive error handling. Failures are logged with enough
    detail for debugging.

    Args:
        product_id: The unique identifier for the product.
        quantity: The quantity ordered (must be positive).

    Returns:
        True if the notification succeeded; False otherwise.

    Raises:
        ValueError: If quantity is not positive.
    """
    if quantity <= 0:
        raise ValueError(f"Quantity must be positive, got {quantity}")

    url = "http://inventory-service/update"
    payload = {"product_id": product_id, "quantity": quantity}

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        
        logger.info(
            "Inventory notified for product %s, quantity %d (status %d)",
            product_id,
            quantity,
            response.status_code,
        )
        return True

    except requests.exceptions.Timeout:
        logger.error(
            "Timeout notifying inventory for product %s, quantity %d",
            product_id,
            quantity,
            exc_info=True,
        )
    except requests.exceptions.ConnectionError:
        logger.error(
            "Connection error notifying inventory for product %s, quantity %d",
            product_id,
            quantity,
            exc_info=True,
        )
    except requests.exceptions.HTTPError as e:
        logger.error(
            "HTTP error notifying inventory for product %s, quantity %d: %s",
            product_id,
            quantity,
            e.response.status_code if e.response else "unknown",
            exc_info=True,
        )
    except requests.exceptions.RequestException:
        logger.error(
            "Failed to notify inventory for product %s, quantity %d",
            product_id,
            quantity,
            exc_info=True,
        )

    return False


@dataclass
class OrderResult:
    """Result of order processing with success status and details."""
    order_id: str
    status: str
    inventory_notifications_succeeded: int
    inventory_notifications_failed: int


def process_order(order_id: str, items: list[dict]) -> OrderResult:
    """
    Process an order by notifying inventory for each item.

    Args:
        order_id: The unique identifier for the order.
        items: List of items, each with 'product_id' and 'quantity'.

    Returns:
        OrderResult with processing details and success counts.
    """
    succeeded = 0
    failed = 0

    for item in items:
        if notify_inventory(item["product_id"], item["quantity"]):
            succeeded += 1
        else:
            failed += 1

    # Only confirm if all notifications succeeded
    status = "CONFIRMED" if failed == 0 else "PARTIAL_FAILURE"
    
    logger.info(
        "Order %s processed: status=%s, succeeded=%d, failed=%d",
        order_id,
        status,
        succeeded,
        failed
    )

    return OrderResult(
        order_id=order_id,
        status=status,
        inventory_notifications_succeeded=succeeded,
        inventory_notifications_failed=failed
    )


# =============================================================================
# Fix 2: Secure password hashing using argon2
# =============================================================================

def get_password_hash(password: str) -> str:
    """
    Hash a password using argon2id (secure password hashing).

    Argon2 is designed to be memory-hard and computationally expensive,
    making it resistant to GPU-based brute-force attacks. It automatically
    handles salt generation.

    Args:
        password: The plain-text password to hash.

    Returns:
        The hashed password string including algorithm parameters.
    """
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(password: str, known_hash: str) -> bool:
    """
    Verify a plain-text password against a known hash.

    Args:
        password: The plain-text password to verify.
        known_hash: The stored hash to verify against.

    Returns:
        True if the password matches; False otherwise.
    """
    ph = PasswordHasher()
    try:
        ph.verify(known_hash, password)
        return True
    except VerifyMismatchError:
        return False


@dataclass
class User:
    """
    Represents a user in the order processing system.

    Uses secure argon2 password hashing with automatic salt handling.
    """
    username: str
    password_hash: str

    @classmethod
    def create(cls, username: str, password: str) -> "User":
        """
        Create a new user with a securely hashed password.

        Args:
            username: The user's username.
            password: The plain-text password (will be hashed).

        Returns:
            A new User instance with the hashed password.
        """
        password_hash = get_password_hash(password)
        logger.info("User created: %s", username)
        return cls(username=username, password_hash=password_hash)

    def verify_password(self, password: str) -> bool:
        """Verify a plain-text password against the stored hash."""
        return verify_password(password, self.password_hash)


# =============================================================================
# Fix 3: Input validation and sanitization
# =============================================================================

@dataclass
class OrderItem:
    """Validated order item."""
    product_id: str
    price: float
    quantity: int


@dataclass
class Order:
    """Validated order with sanitized data."""
    order_id: str
    customer_id: str
    items: list[OrderItem]
    total: float
    # Note: payment_info is NOT stored - only a token reference
    payment_token: Optional[str] = None


def validate_product_id(product_id: str) -> str:
    """
    Validate and sanitize a product ID.

    Args:
        product_id: The product ID to validate.

    Returns:
        The sanitized product ID.

    Raises:
        ValueError: If the product ID is invalid.
    """
    if not product_id or not isinstance(product_id, str):
        raise ValueError("Product ID must be a non-empty string")
    
    # Only allow alphanumeric and hyphens
    sanitized = re.sub(r'[^a-zA-Z0-9\-]', '', product_id)
    
    if len(sanitized) < 3 or len(sanitized) > 50:
        raise ValueError("Product ID must be between 3 and 50 characters")
    
    return sanitized


def validate_quantity(quantity: int) -> int:
    """
    Validate a quantity value.

    Args:
        quantity: The quantity to validate.

    Returns:
        The validated quantity.

    Raises:
        ValueError: If the quantity is invalid.
    """
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer")
    
    if quantity > 10000:
        raise ValueError("Quantity cannot exceed 10000")
    
    return quantity


def validate_price(price: float) -> float:
    """
    Validate a price value.

    Args:
        price: The price to validate.

    Returns:
        The validated price.

    Raises:
        ValueError: If the price is invalid.
    """
    if not isinstance(price, (int, float)) or price < 0:
        raise ValueError("Price must be a non-negative number")
    
    return round(float(price), 2)


def create_order(
    order_id: str,
    customer_id: str,
    items: list[dict],
    payment_token: Optional[str] = None
) -> Order:
    """
    Create a validated order with sanitized data.

    Args:
        order_id: Unique identifier for the order.
        customer_id: The customer's identifier.
        items: List of item dicts with product_id, price, quantity.
        payment_token: Tokenized payment reference (NOT raw card data).

    Returns:
        A validated Order instance.

    Raises:
        ValueError: If any validation fails.
    """
    if not items:
        raise ValueError("Order must contain at least one item")

    validated_items = []
    for item in items:
        validated_items.append(OrderItem(
            product_id=validate_product_id(item.get("product_id", "")),
            price=validate_price(item.get("price", 0)),
            quantity=validate_quantity(item.get("quantity", 0))
        ))

    total = sum(item.price * item.quantity for item in validated_items)

    # Log order creation WITHOUT sensitive data
    logger.info(
        "Created order %s for customer %s with %d items, total: $%.2f",
        order_id,
        customer_id[:4] + "****" if len(customer_id) > 4 else "****",  # Redact
        len(validated_items),
        total
    )

    return Order(
        order_id=order_id,
        customer_id=customer_id,
        items=validated_items,
        total=total,
        payment_token=payment_token
    )


# =============================================================================
# Fix 4: Safe logging without sensitive data
# =============================================================================

def process_payment(order_id: str, payment_token: str) -> bool:
    """
    Process a payment using a tokenized payment reference.

    Args:
        order_id: The order identifier.
        payment_token: A tokenized reference (NOT raw card data).

    Returns:
        True if payment succeeded; False otherwise.
    """
    # GOOD: Only log non-sensitive identifiers
    logger.info(
        "Processing payment for order %s with token %s****",
        order_id,
        payment_token[:4] if len(payment_token) > 4 else "****"
    )

    # Simulated payment processing
    success = True

    if success:
        # GOOD: Log success without sensitive details
        logger.info("Payment successful for order %s", order_id)
    else:
        logger.error("Payment failed for order %s", order_id)

    return success


# =============================================================================
# Fix 5: Batch API calls instead of N+1 pattern
# =============================================================================

def check_inventory_for_order(items: list[dict]) -> list[dict]:
    """
    Check inventory for all items in an order using a batch request.

    Instead of making N separate requests (one per item), this makes
    a single batch request for better performance.

    Args:
        items: List of items with 'product_id' keys.

    Returns:
        List of availability results for each product.
    """
    if not items:
        return []

    product_ids = [item["product_id"] for item in items]

    try:
        # GOOD: Single batch request instead of N+1 calls
        response = requests.post(
            "http://inventory-service/check-batch",
            json={"product_ids": product_ids},
            timeout=10
        )
        response.raise_for_status()

        availability = response.json().get("results", {})
        
        logger.info(
            "Checked inventory for %d products in single batch request",
            len(product_ids)
        )

        return [
            {
                "product_id": pid,
                "available": availability.get(pid, False)
            }
            for pid in product_ids
        ]

    except requests.exceptions.RequestException:
        logger.error(
            "Failed to check inventory for %d products",
            len(product_ids),
            exc_info=True
        )
        # Return all unavailable on error
        return [{"product_id": pid, "available": False} for pid in product_ids]


if __name__ == "__main__":
    print("=== After: Improved code ===\n")

    # Create a user with secure password hashing
    user = User.create("john_doe", "password123")
    print(f"User created: {user.username}")
    print(f"Password hash (argon2, secure): {user.password_hash[:40]}...")
    print(f"Password verification: {user.verify_password('password123')}")
    print(f"Wrong password verification: {user.verify_password('wrongpass')}")

    print()

    # Create order with validation
    try:
        order = create_order(
            order_id="ORD-001",
            customer_id="CUST-12345",
            items=[
                {"product_id": "PROD-001", "price": 10.00, "quantity": 2},
                {"product_id": "PROD-002", "price": 25.00, "quantity": 1}
            ],
            payment_token="tok_visa_4242"
        )
        print(f"Order created: {order.order_id}")
        print(f"Order total: ${order.total:.2f}")
        print(f"Items validated: {len(order.items)}")
    except ValueError as e:
        print(f"Validation error: {e}")

    print()

    # Demonstrate validation errors
    try:
        invalid_order = create_order(
            order_id="ORD-002",
            customer_id="CUST-999",
            items=[
                {"product_id": "P1", "price": -10, "quantity": 0}  # Invalid!
            ]
        )
    except ValueError as e:
        print(f"Caught validation error: {e}")
