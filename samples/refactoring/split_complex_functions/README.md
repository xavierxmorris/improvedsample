# Split Complex Functions

This sample demonstrates how to use GitHub Copilot to break down large, complex functions into smaller, focused units that follow the Single Responsibility Principle.

## Why Split Functions?

| Problem with Large Functions | Benefit of Small Functions |
|------------------------------|---------------------------|
| Hard to test | Easy to unit test in isolation |
| Hard to understand | Clear, focused purpose |
| Hard to reuse | Reusable across codebase |
| Hard to maintain | Easy to modify without side effects |
| Tight coupling | Loose coupling |

## Examples

### 1. Data Processing Pipeline

**Before:** Single function doing cleanse → validate → display

```python
def process_data(item, price):
    # Cleanse data
    item = item.strip()
    price = float(price.strip())
    # Validate data
    if not item:
        raise ValueError("Item name cannot be empty")
    # Display data
    df = pd.DataFrame({'Item': [item], 'Price': [price]})
    print(df.to_string(index=False))
```

**After:** Three focused functions + orchestrator

```python
def cleanse_product_data(item, price) -> tuple[str, float]: ...
def validate_product_data(item, price) -> None: ...
def display_product_data(item, price) -> None: ...

def process_data(item, price):
    item, price = cleanse_product_data(item, price)
    validate_product_data(item, price)
    display_product_data(item, price)
```

### 2. User Registration

**Before:** One function handling validation, normalization, hashing, and creation

**After:**
- `validate_registration_input()` - Input validation
- `normalize_user_data()` - Data normalization
- `hash_password()` - Password hashing
- `create_user()` - User object creation
- `process_user_registration()` - Orchestrates the above

### 3. Sales Analysis

**Before:** One function calculating totals, finding top seller, and printing

**After:**
- `calculate_total_sales()` - Sum all sales
- `find_top_seller()` - Find highest sale
- `calculate_average_sale()` - Calculate average
- `generate_sales_report()` - Create report object
- `print_sales_report()` - Format and print

## Copilot Prompts to Try

1. **Split into specific functions:**
   > "split into 2 separate functions: one for cleansing data, the other for printing"

2. **General splitting:**
   > "break this function into smaller, focused functions"

3. **Extract specific logic:**
   > "extract the validation logic into a separate function"

4. **Use design patterns:**
   > "refactor to use a data class for the return value"

5. **Identify responsibilities:**
   > "what different responsibilities does this function have?"

## Running the Examples

```bash
python before.py
python after.py
```

## Key Takeaways

- **One function, one job** - Each function should do exactly one thing
- **Use data classes** for structured return values
- **Keep the orchestrator** - The original function can call the new helpers
- **Name functions by what they do** - `validate_`, `calculate_`, `format_`, `create_`
- **Functions should be testable in isolation** - No hidden dependencies
