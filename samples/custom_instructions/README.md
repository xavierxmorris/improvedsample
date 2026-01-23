# Custom Instructions Samples

This folder contains examples of custom instructions and prompt files for GitHub Copilot. These files help Copilot understand your project context, coding standards, and common workflows.

## Types of Custom Instructions

### 1. Repository-wide Custom Instructions
**File:** `.github/copilot-instructions.md`

Applies to all requests made in the context of the repository. Use this for:
- Project overview and goals
- Folder structure documentation
- Coding standards and conventions
- Libraries and frameworks used

**Example:** [copilot-instructions.md](./repository-wide/copilot-instructions.md)

### 2. Path-specific Custom Instructions
**Location:** `.github/instructions/*.instructions.md`

Applies to requests for files matching specific paths. Use this for:
- Language-specific guidelines
- Component-specific patterns
- Test file conventions

**Examples:**
- [python.instructions.md](./path-specific/python.instructions.md)
- [react-components.instructions.md](./path-specific/react-components.instructions.md)
- [api-routes.instructions.md](./path-specific/api-routes.instructions.md)

### 3. Prompt Files
**Location:** `.github/prompts/*.prompt.md`

Reusable prompts for common tasks. Use this for:
- Code generation templates
- Review checklists
- Migration guides

**Examples:**
- [new-api-endpoint.prompt.md](./prompt-files/new-api-endpoint.prompt.md)
- [security-review.prompt.md](./prompt-files/security-review.prompt.md)
- [add-unit-tests.prompt.md](./prompt-files/add-unit-tests.prompt.md)

## Best Practices

1. **Keep instructions concise** - Short, self-contained statements work best
2. **Be broadly applicable** - Instructions are sent with every request
3. **Avoid external dependencies** - Don't rely on external resources being available
4. **Update regularly** - Keep instructions in sync with project changes
5. **Test your instructions** - Verify Copilot follows them as expected

## Note

Due to the non-deterministic nature of AI, Copilot may not always follow custom instructions in exactly the same way every time they are used.
