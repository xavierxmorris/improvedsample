# Refactoring Samples

This collection of samples demonstrates how to use GitHub Copilot to refactor code for improved readability, performance, and maintainability.

## Samples Overview

| Sample | Language | Refactoring Technique |
|--------|----------|----------------------|
| [optimize_inefficient](optimize_inefficient/) | Bash/Python | Optimizing inefficient code |
| [cleanup_repeated_code](cleanup_repeated_code/) | Python | Extracting repeated calculations into functions |
| [make_concise](make_concise/) | Python | Making verbose code more concise |
| [split_complex_functions](split_complex_functions/) | Python | Splitting complex functions into smaller units |
| [rewrite_conditionals](rewrite_conditionals/) | Python | Rewriting conditional logic for readability |
| [reformat_structure](reformat_structure/) | Python | Reformatting code to use different structures |

## How to Use These Samples

Each sample contains:
- **`before.py`** (or `.sh`): The original code before refactoring
- **`after.py`** (or `.sh`): The refactored version
- **`README.md`**: Explanation of the refactoring and example Copilot prompts

### Using Copilot to Refactor

1. Open the `before` file in your IDE
2. Select the code you want to refactor
3. Open inline chat:
   - **VS Code**: `Cmd+i` (Mac) or `Ctrl+i` (Windows/Linux)
   - **Visual Studio**: `Alt+/`
   - **JetBrains**: `Ctrl+Shift+i` (Mac) or `Ctrl+Shift+g` (Windows/Linux)
4. Enter the refactoring prompt from the sample's README
5. Review and accept Copilot's suggestion

## Key Refactoring Prompts

| Goal | Example Prompt |
|------|----------------|
| Understand code | `/explain` |
| Optimize performance | `optimize` or `Can this script be improved?` |
| Remove duplication | `move repeated calculations into functions` |
| Simplify code | `make this more concise` |
| Split functions | `split into 2 separate functions: one for X, one for Y` |
| Change conditionals | `rewrite the condition to use a match statement` |
| Change structure | `use arrow notation and better parameter names` |

## Best Practices

1. **Always test refactored code** - Verify the behavior hasn't changed
2. **Refactor incrementally** - Make small changes and test after each
3. **Be specific in prompts** - The more context you provide, the better the suggestions
4. **Review before accepting** - Copilot suggestions are starting points, not final solutions
