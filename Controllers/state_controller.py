from flask import Blueprint, request, jsonify
from init import db
from models.state import States, StateSchema

state_bp = Blueprint('score', __name__, url_prefix='/state')
state_schema = StateSchema()

@state_bp.route("", methods=["POST"])
def create_goal():
    body_data = request.get_json()
        # Check if player_id already exists
    existing_player = States.query.filter_by(state_id=body_data.get('stae_id')).first()
    if existing_player:
        return jsonify({"error": f"state with id {body_data.get('state_id')} already exists"}), 400


    state = States(
        state_id=body_data.get('score_id'),
        goals=body_data.get('goals'),
        points=body_data.get('points'),
        player_id=body_data.get('player_id')
    )
    db.session.add(state)
    db.session.commit()

    return state_schema.jsonify(state), 201

@state_bp.route('/<int:state_id>')
def get_one_card(state_id):
    stmt = db.session.query(States).filter_by(state_id=state_id)
    state = stmt.first()
    if state:
        return state_schema.dump(state)
    else:
        return {"error": f"Player with id {state_id} not found"}, 404

@state_bp.route("/list", methods=["GET"])
def get_all_states():
    all_state = States.query.all()
    serialized_state = state_schema.dump(all_state, many=True)
    return jsonify(serialized_state)

@state_bp.route('/<int:state_id>', methods=['DELETE'])
def delete_player(state_id):
    # Query the player to be deleted
    state = States.query.filter_by(state_id=state_id).first()

    # If player exists, delete it
    if state:
        db.session.delete(state)
        db.session.commit()
        return {"message": f"Player with id {state_id} has been deleted"}, 200
    else:
        return {"error": f"Player with id {state_id} not found"}, 404
