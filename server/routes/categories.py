"""
Categories routes module.
Provides API endpoints for accessing category data.
"""

from flask import Blueprint, jsonify, Response
from typing import List, Dict, Any

from models.category import Category

categories_bp = Blueprint('categories', __name__, url_prefix='/api/categories')


def get_all_categories() -> List[Dict[str, Any]]:
    """
    Retrieve all categories from the database.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing category id and name.
    """
    categories = Category.query.all()
    return [{"id": category.id, "name": category.name} for category in categories]


@categories_bp.route('/', methods=['GET'])
def list_categories() -> tuple[Response, int]:
    """
    Endpoint to get all categories.
    
    Returns:
        Response: JSON response containing a list of all categories with id and name.
    """
    categories = get_all_categories()
    return jsonify(categories), 200
