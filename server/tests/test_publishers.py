"""
Unit tests for the publishers API endpoints.
Tests the functionality of publisher-related routes.
"""

import unittest
from app import app
from models.publisher import Publisher


class TestPublishersEndpoint(unittest.TestCase):
    """Test cases for the publishers API endpoints."""

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

    def test_get_all_publishers_returns_200(self) -> None:
        """Test that the publishers endpoint returns a 200 status code."""
        response = self.client.get('/api/publishers/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_publishers_returns_list(self) -> None:
        """Test that the publishers endpoint returns a list."""
        response = self.client.get('/api/publishers/')
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_publisher_has_required_fields(self) -> None:
        """Test that each publisher in the response has id and name fields."""
        response = self.client.get('/api/publishers/')
        data = response.get_json()
        if len(data) > 0:
            publisher = data[0]
            self.assertIn('id', publisher)
            self.assertIn('name', publisher)


if __name__ == '__main__':
    unittest.main()
