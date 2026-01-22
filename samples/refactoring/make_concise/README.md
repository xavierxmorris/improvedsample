# Make Code More Concise

This sample demonstrates how to use GitHub Copilot to simplify verbose code while maintaining readability.

## Common Verbose Patterns and Their Concise Alternatives

### 1. Unnecessary Intermediate Variables

**Before:**
```python
def calculate_area_of_rectangle(length, width):
    area = length * width
    return area
```

**After:**
```python
def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width
```

### 2. Manual List Building

**Before:**
```python
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
```

**After:**
```python
def get_even_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]
```

### 3. Verbose Boolean Logic

**Before:**
```python
def check_if_adult(age):
    if age >= 18:
        is_adult = True
    else:
        is_adult = False
    return is_adult
```

**After:**
```python
def is_adult(age: int) -> bool:
    return age >= 18
```

### 4. Comparing to True/False

**Before:**
```python
if is_active == True:
    message = "User is active"
```

**After:**
```python
message = "User is active" if is_active else "User is inactive"
```

### 5. Manual File Handling

**Before:**
```python
file_handle = open(file_path, 'r')
contents = file_handle.read()
file_handle.close()
return contents
```

**After:**
```python
with open(file_path, 'r') as f:
    return f.read()
```

## Copilot Prompts to Try

1. **General simplification:**
   > "make this more concise"

2. **Pythonic refactoring:**
   > "rewrite using Pythonic idioms"

3. **List comprehension:**
   > "convert to list comprehension"

4. **Simplify conditionals:**
   > "simplify this boolean logic"

5. **Modern syntax:**
   > "update to use Python 3.10+ syntax"

## Running the Examples

```bash
python before.py
python after.py
```

Both produce identical output.

## Key Takeaways

- **Eliminate intermediate variables** when they don't add clarity
- **Use list/dict/set comprehensions** instead of manual loops
- **Return boolean expressions directly** instead of if/else True/False
- **Use context managers** (`with`) for file operations
- **Use ternary expressions** for simple conditional assignments
- **Choose better function names** (verbs for actions, nouns for getters)
