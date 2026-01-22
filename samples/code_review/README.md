# Code Review Samples

This sample demonstrates how GitHub Copilot code review can automatically catch issues and suggest improvements. It shows before/after examples for common code review concerns:

- **Error handling and logging**
- **Security vulnerabilities**
- **Style conventions (PEP 8/257)**
- **Type hints and documentation**

## Custom Instructions for Copilot Code Review

Custom instructions help Copilot provide more relevant and project-specific feedback. Place these in your repository's `.github/copilot-instructions.md` or configure them in repository settings.

### Example Custom Instructions

```markdown
## Repository context
- This repository implements an order processing system (order intake, payment, fulfillment) where correctness, security, and auditability are critical. 

## Style and conventions
- Follow the PEP 8 and PEP 257 style guide for Python.
- Use clear, domain-relevant names (orders, payments, inventory, customers, shipments).
- Prefer small, focused functions and methods with clearly defined responsibilities.

## Secure coding 
- Verify proper input validation and sanitization.
- Review authentication and authorization logic.

## Error handling guidelines
- Handle timeouts and network errors gracefully.
- Ensure failures are logged with enough detail for debugging.

## Order processing context
- Ensure order creation, payment handling, and updates are idempotent to avoid duplicate orders or duplicate charges.
- Validate and normalize all order, payment, and customer data before persisting or acting on it.
- Do not log or persist sensitive data (passwords, raw payment details, full identifiers) without hashing, encryption, or redaction.
- Call out obvious performance issues in core order workflows (e.g., N+1 queries, per-order synchronous network calls) and suggest simpler, more efficient alternatives.

## Review style
- Be concise, specific and actionable.
- Explain the "why" behind recommendations using bullet points.
```

## Best Practices for Custom Instructions

| Practice | Example |
|----------|---------|
| Use distinct headings | `## Error handling guidelines` |
| Use bullet points | `- Handle timeouts gracefully` |
| Keep instructions short and direct | Avoid lengthy paragraphs |
| Include project context | Domain terms, critical requirements |
| Specify review style | Concise, actionable, explain "why" |

## Files

| File | Description |
|------|-------------|
| `before.py` | Code with issues that Copilot code review would flag |
| `after.py` | Improved code following best practices |

## Examples Covered

### 1. Network Call Error Handling

**Before:** No error handling, no timeout, no logging
```python
def notify_inventory(product_id, quantity):
    requests.post("http://inventory-service/update", 
                  json={"product_id": product_id, "quantity": quantity})
```

**After:** Proper timeout, error handling, logging, and return value
```python
def notify_inventory(product_id: str, quantity: int) -> bool:
    try:
        response = requests.post(url, json=data, timeout=5)
        response.raise_for_status()
        logger.info("Inventory notified...")
        return True
    except requests.exceptions.Timeout:
        logger.error("Timeout notifying inventory...", exc_info=True)
    except requests.exceptions.RequestException:
        logger.error("Failed to notify inventory...", exc_info=True)
    return False
```

### 2. Password Hashing Security

**Before:** Using SHA-256 (too fast, vulnerable to brute-force)
```python
def get_password_hash(password: str, salt: str) -> str:
    return hashlib.sha256((password + salt).encode()).hexdigest()
```

**After:** Using argon2 (designed for password hashing)
```python
from argon2 import PasswordHasher

def get_password_hash(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)
```

## Why This Matters

| Issue | Risk | Solution |
|-------|------|----------|
| No error handling | Unhandled exceptions crash the system | try/except with logging |
| No timeout | Requests hang indefinitely | Set explicit timeout |
| No logging | Can't debug failures | Log success and errors with context |
| SHA-256 for passwords | Brute-force attacks | Use argon2/bcrypt/scrypt |
| No type hints | Unclear API contract | Add type annotations |
| No docstrings | Poor maintainability | Add PEP 257 docstrings |

## Running the Examples

```bash
# Install dependencies
pip install requests argon2-cffi

# Run the examples (after.py will work, before.py may fail without proper setup)
python before.py
python after.py
```

## Copilot Code Review Features

1. **Automatic Reviews** - Copilot reviews PRs automatically when out of draft mode
2. **Custom Instructions** - Tailor feedback to your project's needs
3. **Copilot Autofix** - Suggests fixes for security vulnerabilities found by CodeQL

## Next Steps

1. Create custom instructions for your repository
2. Enable automatic Copilot code review in repository settings
3. Enable code scanning with CodeQL for Copilot Autofix
