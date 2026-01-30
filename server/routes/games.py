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


@games_bp.route('/api/games', methods=['POST'])
def create_game() -> tuple[Response, int]:
    """
    Create a new game.
    
    Expected JSON body:
        title (str): The title of the game (required, min 2 characters).
        description (str): The description of the game (required, min 10 characters).
        category_id (int): The ID of the category (required).
        publisher_id (int): The ID of the publisher (required).
        star_rating (float, optional): The star rating of the game (0-5).
    
    Returns:
        Response: JSON object with the created game data and 201 status code.
        Error responses: 400 for validation errors, 404 for invalid category/publisher.
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        required_fields = ['title', 'description', 'category_id', 'publisher_id']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400
        
        # Validate category and publisher exist
        category = Category.query.get(data['category_id'])
        if not category:
            return jsonify({"error": "Category not found"}), 404
        
        publisher = Publisher.query.get(data['publisher_id'])
        if not publisher:
            return jsonify({"error": "Publisher not found"}), 404
        
        # Validate star_rating if provided
        star_rating = data.get('star_rating')
        if star_rating is not None:
            try:
                star_rating = float(star_rating)
                if star_rating < 0 or star_rating > 5:
                    return jsonify({"error": "Star rating must be between 0 and 5"}), 400
            except (ValueError, TypeError):
                return jsonify({"error": "Star rating must be a number"}), 400
        
        # Create new game
        new_game = Game(
            title=data['title'],
            description=data['description'],
            category_id=data['category_id'],
            publisher_id=data['publisher_id'],
            star_rating=star_rating
        )
        
        db.session.add(new_game)
        db.session.commit()
        
        # Return the created game
        game_query = get_games_base_query().filter(Game.id == new_game.id).first()
        return jsonify(game_query.to_dict()), 201
        
    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the game"}), 500


@games_bp.route('/api/games/<int:id>', methods=['PUT'])
def update_game(id: int) -> tuple[Response, int]:
    """
    Update an existing game.
    
    Args:
        id: The ID of the game to update.
    
    Expected JSON body (all fields optional):
        title (str): The title of the game (min 2 characters).
        description (str): The description of the game (min 10 characters).
        category_id (int): The ID of the category.
        publisher_id (int): The ID of the publisher.
        star_rating (float): The star rating of the game (0-5).
    
    Returns:
        Response: JSON object with the updated game data and 200 status code.
        Error responses: 400 for validation errors, 404 for game/category/publisher not found.
    """
    try:
        # Find the game
        game = Game.query.get(id)
        if not game:
            return jsonify({"error": "Game not found"}), 404
        
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Request body is required"}), 400
        
        # Update title if provided
        if 'title' in data:
            game.title = data['title']
        
        # Update description if provided
        if 'description' in data:
            game.description = data['description']
        
        # Update category_id if provided
        if 'category_id' in data:
            category = Category.query.get(data['category_id'])
            if not category:
                return jsonify({"error": "Category not found"}), 404
            game.category_id = data['category_id']
        
        # Update publisher_id if provided
        if 'publisher_id' in data:
            publisher = Publisher.query.get(data['publisher_id'])
            if not publisher:
                return jsonify({"error": "Publisher not found"}), 404
            game.publisher_id = data['publisher_id']
        
        # Update star_rating if provided
        if 'star_rating' in data:
            star_rating = data['star_rating']
            if star_rating is not None:
                try:
                    star_rating = float(star_rating)
                    if star_rating < 0 or star_rating > 5:
                        return jsonify({"error": "Star rating must be between 0 and 5"}), 400
                    game.star_rating = star_rating
                except (ValueError, TypeError):
                    return jsonify({"error": "Star rating must be a number"}), 400
            else:
                game.star_rating = star_rating
        
        db.session.commit()
        
        # Return the updated game
        game_query = get_games_base_query().filter(Game.id == id).first()
        return jsonify(game_query.to_dict()), 200
        
    except ValueError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while updating the game"}), 500


@games_bp.route('/api/games/<int:id>', methods=['DELETE'])
def delete_game(id: int) -> tuple[Response, int]:
    """
    Delete a game by ID.
    
    Args:
        id: The ID of the game to delete.
    
    Returns:
        Response: JSON object with success message and 200 status code.
        Error responses: 404 if game not found.
    """
    try:
        game = Game.query.get(id)
        if not game:
            return jsonify({"error": "Game not found"}), 404
        
        db.session.delete(game)
        db.session.commit()
        
        return jsonify({"message": "Game deleted successfully"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while deleting the game"}), 500
