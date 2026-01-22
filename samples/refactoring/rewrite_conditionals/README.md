# Rewrite Conditional Code

This sample demonstrates how to use GitHub Copilot to rewrite conditional logic for better readability using Python 3.10+ pattern matching and data-driven approaches.

## Techniques Demonstrated

### 1. Pattern Matching (match/case)

Python 3.10+ introduces structural pattern matching, which can replace long if/elif chains.

**Before:**
```python
if animal is None:
    return "Unknown"
elif animal.lower() == "dog":
    return "Bark"
elif animal.lower() == "cat":
    return "Meow"
# ... more elif
```

**After:**
```python
match animal:
    case None:
        return "Unknown"
    case str(a) if a.lower() == "dog":
        return "Bark"
    case str(a) if a.lower() == "cat":
        return "Meow"
    case _:
        return "Unknown"
```

### 2. Dictionary Lookup

For simple value mappings, dictionaries are often cleaner than any conditional.

**Before:**
```python
if command == "add":
    # ...
elif command == "subtract":
    # ...
```

**After:**
```python
ANIMAL_SOUNDS = {"dog": "Bark", "cat": "Meow", "bird": "Tweet"}

def get_animal_sound(animal):
    return ANIMAL_SOUNDS.get(animal.lower(), "Unknown")
```

### 3. Data-Driven Conditionals

Move the logic into data structures for cleaner, more maintainable code.

**Before:**
```python
if score >= 90:
    return "A"
elif score >= 80:
    return "B"
# ...
```

**After:**
```python
GRADE_BOUNDARIES = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]

def get_grade(score):
    for min_score, grade in GRADE_BOUNDARIES:
        if score >= min_score:
            return grade
```

### 4. Pattern Matching with Destructuring

Match on tuple structures and lists:

```python
match (command, args):
    case ("add", [a, b, *_]):
        return str(float(a) + float(b))
    case ("divide", [a, b, *_]) if float(b) != 0:
        return str(float(a) / float(b))
```

## Copilot Prompts to Try

1. **Convert to match/case:**
   > "rewrite the condition to use a match statement"

2. **Use dictionary lookup:**
   > "refactor to use a dictionary instead of if/elif"

3. **Data-driven approach:**
   > "extract the conditional values into a data structure"

4. **Modern Python syntax:**
   > "rewrite using Python 3.10+ pattern matching with guards"

5. **Combine transformations:**
   > "rewrite the condition to use a switch and add documentation"

## Running the Examples

```bash
# Requires Python 3.10+ for pattern matching
python before.py
python after.py
```

Both produce identical output.

## When to Use Each Approach

| Pattern | Best For |
|---------|----------|
| `match/case` | Complex branching, type checking, destructuring |
| Dictionary lookup | Simple value-to-value mappings |
| Data-driven | Range checks, threshold-based decisions |
| Original if/elif | Simple cases, backward compatibility |

## Key Takeaways

- **Pattern matching** makes complex conditionals more readable
- **Dictionaries** are perfect for mapping values
- **Data structures** can replace nested conditionals
- **Guards** (`if` in case clauses) handle complex conditions
- **Wildcard `_`** handles default cases
