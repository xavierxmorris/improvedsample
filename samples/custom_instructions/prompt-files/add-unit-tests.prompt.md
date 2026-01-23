# Add Unit Tests

Your goal is to generate comprehensive unit tests for the specified code.

## Test Framework

- Use **pytest** for Python code
- Use **Playwright** for end-to-end tests
- Use testing utilities from the existing test files

## Test Coverage Requirements

### For API Routes

Test all HTTP methods with:
- **Happy path** - Valid requests return expected data
- **Not found** - Invalid IDs return 404
- **Validation errors** - Invalid input returns 400
- **Edge cases** - Empty lists, boundary values

### For Models

- Test model creation with valid data
- Test required field validation
- Test `to_dict()` serialization
- Test relationships between models

### For Utility Functions

- Test with typical inputs
- Test with edge cases (empty, null, max values)
- Test error conditions

## Python Test Template

```python
"""
Unit tests for {module_name}.

This module contains tests for the {description} functionality.
"""

import pytest
from flask import Flask
from models import {Model}
from routes import {blueprint}


@pytest.fixture
def app():
    """Create test application."""
    app = Flask(__name__)
    app.config["TESTING"] = True
    # Configure test database
    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


class TestGet{Resource}:
    """Tests for GET /{resource} endpoints."""

    def test_list_returns_all_items(self, client):
        """Should return all {resource} items."""
        response = client.get("/{resource}/")
        assert response.status_code == 200
        data = response.get_json()
        assert "data" in data

    def test_get_by_id_returns_item(self, client):
        """Should return single {resource} by ID."""
        response = client.get("/{resource}/1")
        assert response.status_code == 200

    def test_get_nonexistent_returns_404(self, client):
        """Should return 404 for nonexistent {resource}."""
        response = client.get("/{resource}/99999")
        assert response.status_code == 404


class TestCreate{Resource}:
    """Tests for POST /{resource} endpoints."""

    def test_create_with_valid_data(self, client):
        """Should create {resource} with valid data."""
        data = {"name": "Test", "description": "Test description"}
        response = client.post("/{resource}/", json=data)
        assert response.status_code == 201

    def test_create_missing_required_field(self, client):
        """Should return 400 when required field is missing."""
        data = {"description": "Missing name"}
        response = client.post("/{resource}/", json=data)
        assert response.status_code == 400
```

## Naming Conventions

- Test files: `test_{module}.py`
- Test classes: `Test{Feature}` or `Test{Method}`
- Test functions: `test_{scenario}` or `test_{method}_{condition}`

## Running Tests

```bash
# Run all tests
./scripts/run-server-tests.sh

# Run specific test file
pytest server/tests/test_{module}.py -v

# Run with coverage
pytest --cov=server --cov-report=html
```
