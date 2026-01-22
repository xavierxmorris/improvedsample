"""
Publishers routes module.
Provides API endpoints for accessing publisher data.
"""

from flask import Blueprint, jsonify
from typing import List, Dict, Any

from models.publisher import Publisher

publishers_bp = Blueprint('publishers', __name__, url_prefix='/api/publishers')


def get_all_publishers() -> List[Dict[str, Any]]:
    """
    Retrieve all publishers from the database.
    
    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing publisher id and name.
    """
    publishers = Publisher.query.all()
    return [{"id": publisher.id, "name": publisher.name} for publisher in publishers]


@publishers_bp.route('/', methods=['GET'])
def list_publishers():
    """
    Endpoint to get all publishers.
    
    Returns:
        Response: JSON response containing a list of all publishers with id and name.
    """
    publishers = get_all_publishers()
    return jsonify(publishers), 200
