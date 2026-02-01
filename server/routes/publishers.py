"""
Publishers API routes.
This module handles endpoints related to game publishers.
"""

from flask import Blueprint, jsonify
from models.publisher import Publisher

publishers_bp = Blueprint('publishers', __name__)


@publishers_bp.route('/api/publishers', methods=['GET'])
def get_publishers() -> tuple:
    """
    Get all publishers.
    
    Returns:
        tuple: JSON response with list of publishers and HTTP status code
    """
    publishers = Publisher.query.all()
    return jsonify([{
        'id': publisher.id,
        'name': publisher.name
    } for publisher in publishers]), 200
