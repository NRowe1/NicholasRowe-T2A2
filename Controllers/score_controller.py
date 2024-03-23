from flask import Blueprint, request, jsonify
from init import db
from models.score import Score, ScoreSchema

goal_bp = Blueprint('score', __name__, url_prefix='/score')
goal_schema = ScoreSchema()

@goal_bp.route("", methods=["POST"])
def create_goal():
    body_data = request.get_json()
        # Check if player_id already exists
    existing_player = Score.query.filter_by(score_id=body_data.get('score_id')).first()
    if existing_player:
        return jsonify({"error": f"goal with id {body_data.get('score_id')} already exists"}), 400


    goal = Score(
        score_id=body_data.get('score_id'),
        goals=body_data.get('goals'),
        points=body_data.get('points'),
        player_id=body_data.get('player_id')
    )
    db.session.add(goal)
    db.session.commit()

    return goal_schema.jsonify(goal), 201

@goal_bp.route('/<int:score_id>')
def get_one_card(score_id):
    stmt = db.session.query(Score).filter_by(score_id=score_id)
    player = stmt.first()
    if player:
        return goal_schema.dump(player)
    else:
        return {"error": f"Player with id {score_id} not found"}, 404

@goal_bp.route("/list", methods=["GET"])
def get_all_goals():
    all_goals = Score.query.all()
    serialized_goals = goal_schema.dump(all_goals, many=True)
    return jsonify(serialized_goals)

@goal_bp.route('/<int:score_id>', methods=['DELETE'])
def delete_player(score_id):
    # Query the player to be deleted
    goal = Score.query.filter_by(score_id=score_id).first()

    # If player exists, delete it
    if goal:
        db.session.delete(goal)
        db.session.commit()
        return {"message": f"Player with id {score_id} has been deleted"}, 200
    else:
        return {"error": f"Player with id {score_id} not found"}, 404
