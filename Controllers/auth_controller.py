from flask import Blueprint, request, jsonify
from init import db
from models.player import Player, PlayerSchema

player_bp = Blueprint('player', __name__, url_prefix='/player')
player_schema = PlayerSchema()

@player_bp.route("", methods=["POST"])
def player_register():
    # Get data from the request body
    body_data = request.get_json()

    # Check if player_id already exists
    existing_player = Player.query.filter_by(player_id=body_data.get('player_id')).first()
    if existing_player:
        return jsonify({"error": f"Player with id {body_data.get('player_id')} already exists"}), 400

    # Create a new player instance
    player = Player(
        player_id=body_data.get('player_id'),
        first_name=body_data.get('first_name'),
        last_name=body_data.get('last_name'),
        position=body_data.get('position'),
        jersey_number=body_data.get('jersey_number')
    )

    # Add player to the database
    db.session.add(player)
    db.session.commit()

    # Respond with serialized player data
    return player_schema.dump(player), 201

@player_bp.route('/<int:player_id>')
def get_one_card(player_id):
    stmt = db.session.query(Player).filter_by(player_id=player_id)
    player = stmt.first()
    if player:
        return player_schema.dump(player)
    else:
        return {"error": f"Player with id {player_id} not found"}, 404
    
@player_bp.route("/list", methods=["GET"])
def get_all_players():
    # Query all players from the database
    all_players = Player.query.all()
    
    # Serialize the players using the player schema
    serialized_players = player_schema.dump(all_players, many=True)
    
    # Return the serialized players as a JSON response
    return jsonify(serialized_players)

@player_bp.route('/<int:player_id>', methods=['DELETE'])
def delete_player(player_id):
    # Query the player to be deleted
    player = Player.query.filter_by(player_id=player_id).first()

    # If player exists, delete it
    if player:
        db.session.delete(player)
        db.session.commit()
        return {"message": f"Player with id {player_id} has been deleted"}, 200
    else:
        return {"error": f"Player with id {player_id} not found"}, 404
    

    