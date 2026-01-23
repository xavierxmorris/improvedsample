# API Routes Instructions

These instructions apply to Flask route files.

---
applyTo: "server/routes/**/*.py"
---

## Blueprint Structure

- Create one blueprint per resource (games, publishers, categories)
- Use consistent URL prefixes matching the resource name
- Register blueprints in the main app file

## RESTful Conventions

Follow RESTful API design:
- `GET /resources` - List all resources
- `GET /resources/<id>` - Get single resource
- `POST /resources` - Create new resource
- `PUT /resources/<id>` - Update resource
- `DELETE /resources/<id>` - Delete resource

## Response Format

- Return JSON responses with consistent structure
- Include appropriate HTTP status codes
- Use `jsonify()` for all responses

Success response:
```python
return jsonify({"data": result}), 200
```

Error response:
```python
return jsonify({"error": "Resource not found"}), 404
```

## Error Handling

- Use try-except blocks for database operations
- Return 400 for validation errors
- Return 404 for missing resources
- Return 500 for unexpected errors
- Log all errors with context

## Validation

- Validate all input data before processing
- Check required fields are present
- Validate data types and formats
- Return descriptive error messages

## Example Route

```python
@games_bp.route("/<int:game_id>", methods=["GET"])
def get_game(game_id: int) -> tuple[Response, int]:
    """Get a single game by ID.

    Args:
        game_id: The unique identifier of the game.

    Returns:
        JSON response with game data or error message.
    """
    try:
        game = Game.query.get(game_id)
        if not game:
            return jsonify({"error": "Game not found"}), 404
        return jsonify({"data": game.to_dict()}), 200
    except Exception as e:
        logger.error(f"Error fetching game {game_id}: {e}")
        return jsonify({"error": "Internal server error"}), 500
```
