# Clean Up Repeated Code

This sample demonstrates how to use GitHub Copilot to identify and extract repeated calculations into reusable functions.

## The Problem

Repeated code (violating the DRY principle) leads to:
- **Maintenance burden**: Changes must be made in multiple places
- **Bug risk**: Easy to update one instance and forget another
- **Readability issues**: Harder to understand the code's intent

## Examples

### Sales Calculation

**Before:**
```python
total_sales += apple_price * apples_sold
total_sales += orange_price * oranges_sold
total_sales += banana_price * bananas_sold
```

**After:**
```python
def calculate_sales(price: float, quantity: int) -> float:
    return price * quantity

total_sales += calculate_sales(price=3, quantity=100)
total_sales += calculate_sales(price=5, quantity=50)
```

### Discount Calculation

**Before:**
```python
item1_discount = item1_price * (item1_discount_percent / 100)
item1_final = item1_price - item1_discount
# ... repeated for each item
```

**After:**
```python
def calculate_discounted_price(price: float, discount_percent: float) -> tuple:
    discount = price * (discount_percent / 100)
    return discount, price - discount
```

## Copilot Prompts to Try

1. **Extract repeated calculations:**
   > "move repeated calculations into functions"

2. **Identify DRY violations:**
   > "identify repeated code patterns in this file"

3. **Refactor with data structures:**
   > "refactor to use a list of items instead of individual variables"

4. **Add type hints:**
   > "extract into a function with proper type hints and docstring"

## Running the Examples

```bash
python before.py
python after.py
```

Both should produce identical output, but the `after.py` version is more maintainable.

## Key Takeaways

- **Extract repeated patterns** into functions with descriptive names
- **Use data structures** (lists, dicts) instead of numbered variables
- **Add type hints** to make functions self-documenting
- **Keep functions focused** on a single responsibility
