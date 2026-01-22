# Optimize Inefficient Code

This sample demonstrates how to use GitHub Copilot to identify and fix performance issues in code.

## Examples

### Bash Script Optimization

**Before (`before.sh`):**
```bash
for file in $(find . -type f -name "*.txt"); do
    wc -l "$file"
done
```

**After (`after.sh`):**
```bash
find . -type f -name "*.txt" -exec wc -l {} +
```

**Why it's better:** Using `-exec ... +` passes multiple files to `wc` at once, reducing process spawning overhead.

### Python Optimization

| Function | Before | After | Improvement |
|----------|--------|-------|-------------|
| `find_duplicates` | O(n²) nested loops | O(n) with Counter | Much faster for large lists |
| `count_word_frequency` | Manual dict updates | Counter | Cleaner and optimized |
| `filter_and_transform` | Multiple loops | List comprehension | Single pass, more Pythonic |

## Copilot Prompts to Try

1. **Ask if code can be improved:**
   > "Can this script be improved?"

2. **Request optimization:**
   > "optimize"

3. **Identify performance issues:**
   > "What are the performance issues in this code?"

4. **Suggest better data structures:**
   > "Suggest better data structures for this algorithm"

## Running the Examples

```bash
# Bash examples
chmod +x before.sh after.sh
./before.sh
./after.sh

# Python examples
python before.py
python after.py
```

## Key Takeaways

- **Use built-in functions**: Python's `Counter`, `set`, comprehensions are optimized
- **Avoid nested loops**: Look for O(n²) patterns and reduce to O(n) when possible
- **Minimize process spawning**: In shell scripts, batch operations when possible
- **Use appropriate data structures**: Sets for membership tests, dicts for lookups
