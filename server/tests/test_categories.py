"""
Unit tests for the categories API endpoints.
Tests the functionality of category-related routes.
"""

import unittest
from app import app
from models.category import Category


class TestCategoriesEndpoint(unittest.TestCase):
    """Test cases for the categories API endpoints."""

    def setUp(self) -> None:
        """Set up test fixtures before each test method."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        """Clean up after each test method."""
        self.app_context.pop()

    def test_get_all_categories_returns_200(self) -> None:
        """Test that the categories endpoint returns a 200 status code."""
        response = self.client.get('/api/categories/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_categories_returns_list(self) -> None:
        """Test that the categories endpoint returns a list."""
        response = self.client.get('/api/categories/')
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_category_has_required_fields(self) -> None:
        """Test that each category in the response has id and name fields."""
        response = self.client.get('/api/categories/')
        data = response.get_json()
        if len(data) > 0:
            category = data[0]
            self.assertIn('id', category)
            self.assertIn('name', category)


if __name__ == '__main__':
    unittest.main()
