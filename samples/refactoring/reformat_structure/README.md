# Reformat Code Structure

This sample demonstrates how to use GitHub Copilot to reformat code to use more modern, idiomatic Python structures.

## Transformations Demonstrated

### 1. Better Parameter Names

**Before:**
```python
def list_repos(o, p):
    url = f"https://api.github.com/orgs/{o}/repos?per_page={int(p)}"
```

**After:**
```python
def list_repositories(organization: str, per_page: int) -> list[dict]:
    url = f"https://api.github.com/orgs/{organization}/repos?per_page={per_page}"
```

### 2. String Formatting

**Before:**
```python
info = 'Name: ' + name + ', Email: ' + email
```

**After:**
```python
info = f"Name: {name}, Email: {email}"
```

### 3. List Comprehensions

**Before:**
```python
results = []
for n in numbers:
    if n > 0:
        squared = n * n
        results.append(squared)
```

**After:**
```python
results = [n ** 2 for n in numbers if n > 0]
```

### 4. Ternary Expressions

**Before:**
```python
if formal == True:
    greeting = 'Dear ' + name
else:
    greeting = 'Hi ' + name
```

**After:**
```python
greeting = f"Dear {name}" if formal else f"Hi {name}"
```

### 5. Dataclasses

**Before:**
```python
class OldStyleClass:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return 'OldStyleClass(name=' + self.name + ...
    
    def __eq__(self, other):
        ...
```

**After:**
```python
@dataclass
class Person:
    name: str
    age: int
    email: str
    # __init__, __repr__, __eq__ auto-generated!
```

### 6. Context Managers

**Before:**
```python
f = open(filename, 'r')
content = f.read()
f.close()
```

**After:**
```python
with open(filename, 'r') as f:
    return f.read()
```

### 7. Generator with next()

**Before:**
```python
found = None
for item in items:
    if item['id'] == target:
        found = item
        break
return found
```

**After:**
```python
return next((item for item in items if item['id'] == target), None)
```

### 8. Functional Patterns

**Before:**
```python
total = 0
for item in items:
    total = total + item['price'] * item['quantity']
```

**After:**
```python
# Option 1: sum with generator
return sum(item['price'] * item['quantity'] for item in items)

# Option 2: reduce
return reduce(lambda t, i: t + i['price'] * i['quantity'], items, 0)
```

## Copilot Prompts to Try

1. **Better naming:**
   > "use descriptive parameter names and add type hints"

2. **Modern string formatting:**
   > "convert string concatenation to f-strings"

3. **Functional style:**
   > "use list comprehension instead of for loop"

4. **Dataclass conversion:**
   > "convert this class to a dataclass"

5. **General modernization:**
   > "refactor to use modern Python 3.10+ patterns"

6. **Arrow notation (for other languages):**
   > "use arrow notation and better parameter names"

## Running the Examples

```bash
python before.py
python after.py
```

## Key Takeaways

| Old Pattern | Modern Pattern |
|-------------|----------------|
| String concatenation | f-strings |
| Manual loops | List/dict comprehensions |
| if/else blocks | Ternary expressions |
| Boilerplate classes | @dataclass |
| open/close | Context managers |
| Loop to find | next() with generator |
| Single-letter params | Descriptive names |
| No types | Type hints |
