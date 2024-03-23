from flask import Blueprint, request, jsonify
from init import db
from models.team import Team, TeamSchema

team_bp = Blueprint('team', __name__, url_prefix='/team')
team_schema = TeamSchema()

@team_bp.route("", methods=["POST"])
def create_goal():
    body_data = request.get_json()
        # Check if player_id already exists
    existing_player = Team.query.filter_by(team_id=body_data.get('team_id')).first()
    if existing_player:
        return jsonify({"error": f"goal with id {body_data.get('team_id')} already exists"}), 400


    team = Team(
        team_id=body_data.get('team_id'),
        team_name=body_data.get('Team_name'),
    )
    db.session.add(team)
    db.session.commit()

    return team_schema.jsonify(team), 201

@team_bp.route('/<int:team_id>')
def get_one_card(team_id):
    stmt = db.session.query(Team).filter_by(score_id=team_id)
    player = stmt.first()
    if player:
        return team_schema.dump(player)
    else:
        return {"error": f"Team with id {team_id} not found"}, 404

@team_bp.route("/list", methods=["GET"])
def get_all_goals():
    all_teams = Team.query.all()
    serialized_goals = team_schema.dump(all_teams, many=True)
    return jsonify(serialized_goals)

@team_bp.route('/<int:team_id>', methods=['DELETE'])
def delete_player(team_id):
    # Query the player to be deleted
    team = Team.query.filter_by(team_id=team_id).first()

    # If player exists, delete it
    if team:
        db.session.delete(team)
        db.session.commit()
        return {"message": f"Team with id {team_id} has been deleted"}, 200
    else:
        return {"error": f"Team with id {team_id} not found"}, 404
