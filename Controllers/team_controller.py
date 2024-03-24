from flask import Blueprint, request, jsonify
from init import db
from models.team import Team, TeamSchema

team_bp = Blueprint('team', __name__, url_prefix='/team')
team_schema = TeamSchema()

@team_bp.route("", methods=["POST"])
def create_team():
    data = request.get_json()
    existing_team = Team.query.filter_by(team_id=data.get('team_id')).first()
    if existing_team:
        return jsonify({"error": f"Team with id {data.get('team_id')} already exists"}), 400

    team = Team(
        team_id=data.get('team_id'),
        team_name=data.get('team_name'),
    )
    db.session.add(team)
    db.session.commit()

    return team_schema.jsonify(team), 201

@team_bp.route('/<int:team_id>')
def get_one_team(team_id):
    team = Team.query.get(team_id)
    if team:
        return team_schema.jsonify(team)
    else:
        return {"error": f"Team with id {team_id} not found"}, 404

@team_bp.route("/list", methods=["GET"])
def get_all_teams():
    all_teams = Team.query.all()
    serialized_teams = team_schema.dump(all_teams, many=True)
    return jsonify(serialized_teams)

@team_bp.route('/<int:team_id>', methods=['DELETE'])
def delete_team(team_id):
    team = Team.query.get(team_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return {"message": f"Team with id {team_id} has been deleted"}, 200
    else:
        return {"error": f"Team with id {team_id} not found"}, 404
