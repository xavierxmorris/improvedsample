# Python Code Instructions

These instructions apply to all Python files in the project.

---
applyTo: "**/*.py"
---

## Type Hints

- Always use type hints for function parameters and return values
- Use `Optional[T]` for nullable parameters
- Use `list[T]` instead of `List[T]` (Python 3.9+)
- Use `dict[K, V]` instead of `Dict[K, V]` (Python 3.9+)

## Documentation

- Every function must have a docstring
- Use Google-style docstrings format
- Document parameters, return values, and exceptions

Example:
```python
def calculate_funding_progress(raised: float, goal: float) -> float:
    """Calculate the funding progress percentage.

    Args:
        raised: The amount raised so far.
        goal: The funding goal amount.

    Returns:
        The progress as a percentage (0-100).

    Raises:
        ValueError: If goal is zero or negative.
    """
```

## File Structure

- Add a module docstring at the top of each file
- Group imports: standard library, third-party, local
- Separate import groups with blank lines

## Error Handling

- Use specific exception types, not bare `except`
- Log errors with appropriate context
- Return meaningful error messages in API responses

## Testing

- Use pytest for all tests
- Name test files with `test_` prefix
- Name test functions with `test_` prefix
- Use fixtures for common setup
