"""
Games routes module.
Provides API endpoints for accessing game data with optional filtering by category and publisher.
"""

from flask import jsonify, Response, Blueprint, request
from models import db, Game, Publisher, Category
from sqlalchemy.orm import Query
from typing import Optional

# Create a Blueprint for games routes
games_bp = Blueprint('games', __name__)


def get_games_base_query() -> Query:
    """
    Create the base query for retrieving games with joined publisher and category data.
    
    Returns:
        Query: SQLAlchemy query object with Game, Publisher, and Category joins.
    """
    return db.session.query(Game).join(
        Publisher, 
        Game.publisher_id == Publisher.id, 
        isouter=True
    ).join(
        Category, 
        Game.category_id == Category.id, 
        isouter=True
    )


def apply_filters(query: Query, category_id: Optional[int], publisher_id: Optional[int]) -> Query:
    """
    Apply optional category and publisher filters to a games query.
    
    Args:
        query: The base SQLAlchemy query to filter.
        category_id: Optional category ID to filter by.
        publisher_id: Optional publisher ID to filter by.
    
    Returns:
        Query: The filtered query object.
    """
    if category_id is not None:
        query = query.filter(Game.category_id == category_id)
    if publisher_id is not None:
        query = query.filter(Game.publisher_id == publisher_id)
    return query


@games_bp.route('/api/games', methods=['GET'])
def get_games() -> Response:
    """
    Retrieve all games, optionally filtered by category and/or publisher.
    
    Query Parameters:
        category_id (int, optional): Filter games by category ID.
        publisher_id (int, optional): Filter games by publisher ID.
    
    Returns:
        Response: JSON array of game objects.
    """
    # Parse optional filter parameters
    category_id: Optional[int] = request.args.get('category_id', type=int)
    publisher_id: Optional[int] = request.args.get('publisher_id', type=int)
    
    # Build and execute the filtered query
    query = get_games_base_query()
    query = apply_filters(query, category_id, publisher_id)
    games_query = query.all()
    
    # Convert the results using the model's to_dict method
    games_list = [game.to_dict() for game in games_query]
    
    return jsonify(games_list)

@games_bp.route('/api/games/<int:id>', methods=['GET'])
def get_game(id: int) -> tuple[Response, int] | Response:
    # Use the base query and add filter for specific game
    game_query = get_games_base_query().filter(Game.id == id).first()
    
    # Return 404 if game not found
    if not game_query: 
        return jsonify({"error": "Game not found"}), 404
    
    # Convert the result using the model's to_dict method
    game = game_query.to_dict()
    
    return jsonify(game)
