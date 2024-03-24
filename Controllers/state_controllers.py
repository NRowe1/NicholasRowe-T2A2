from flask import Blueprint, request, jsonify
from init import db
from models.games import Games, GamesSchema

game_bp = Blueprint('team', __name__, url_prefix='/team')
game_schema = GamesSchema()

@game_bp.route("", methods=["POST"])
def create_game():
    data = request.get_json()
    existing_team = Games.query.filter_by(game_id=data.get('game_id')).first()
    if existing_team:
        return jsonify({"error": f"Game with id {data.get('game_id')} already exists"}), 400

    game = Games(
        team_id=data.get('game_id'),
        date=data.get('date'),
        time=data.get('time'),
        location=data.get('location')
    )
    db.session.add(game)
    db.session.commit()

    return game_schema.jsonify(game), 201


@game_bp.route("/list", methods=["GET"])
def get_all_games():
    all_games = Games.query.all()
    serialized_games = game_schema.dump(all_games, many=True)
    return jsonify(serialized_games)

@game_bp.route('/<int:team_id>', methods=['DELETE'])
def delete_game(game_id):
    team = Games.query.get(game_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return {"message": f"Games with id {game_id} has been deleted"}, 200
    else:
        return {"error": f"Games with id {game_id} not found"}, 404
