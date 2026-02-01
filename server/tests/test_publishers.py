"""
Unit tests for the publishers API endpoints.
This module tests the publishers routes functionality.
"""

import unittest
from app import app
from models.publisher import Publisher


class PublishersTestCase(unittest.TestCase):
    """Test case for publishers API endpoints."""

    def setUp(self) -> None:
        """Set up test client and database."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        """Clean up after tests."""
        self.app_context.pop()

    def test_get_publishers(self) -> None:
        """Test getting all publishers."""
        # Get publishers
        response = self.client.get('/api/publishers')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)
        # Verify structure if publishers exist
        if len(data) > 0:
            self.assertIn('id', data[0])
            self.assertIn('name', data[0])

    def test_get_publishers_returns_list(self) -> None:
        """Test getting publishers returns a list."""
        response = self.client.get('/api/publishers')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        self.assertIsInstance(data, list)


if __name__ == '__main__':
    unittest.main()
