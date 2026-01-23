# New API Endpoint

Your goal is to generate a new Flask API endpoint following RESTful conventions.

## Required Information

Ask for the following if not provided:
- Resource name (e.g., "pledges", "comments")
- Operations needed (list, get, create, update, delete)
- Data fields and their types

## Implementation Requirements

### Route Structure

1. Create a new blueprint in `server/routes/`
2. Follow the naming pattern: `{resource}.py`
3. Register the blueprint in `server/app.py`

### Code Standards

- Use type hints for all parameters and return values
- Add docstrings to all functions
- Include a file header comment explaining the purpose

### Response Format

```python
# Success responses
return jsonify({"data": result}), 200  # GET
return jsonify({"data": result}), 201  # POST (created)
return jsonify({"message": "Deleted"}), 200  # DELETE

# Error responses
return jsonify({"error": "Validation failed", "details": errors}), 400
return jsonify({"error": "Not found"}), 404
return jsonify({"error": "Internal server error"}), 500
```

### Database Model

If a new model is needed:
1. Create in `server/models/{resource}.py`
2. Inherit from `Base` class
3. Include `to_dict()` method for serialization
4. Import and register in `server/models/__init__.py`

### Testing

Generate corresponding tests in `server/tests/test_{resource}.py`:
- Test all CRUD operations
- Test error cases (404, 400)
- Test validation logic

## Template

```python
"""
{Resource} API routes.

This module provides REST API endpoints for managing {resource} records.
"""

from flask import Blueprint, jsonify, request, Response
from models import {Model}
from utils.database import db

{resource}_bp = Blueprint("{resource}", __name__, url_prefix="/{resource}")


@{resource}_bp.route("/", methods=["GET"])
def list_{resource}() -> tuple[Response, int]:
    """List all {resource} records."""
    # Implementation here
    pass
```
