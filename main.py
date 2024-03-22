import os
from flask import Flask
from marshmallow.exceptions import ValidationError

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    # Load configurations from environment variables
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    # Connect libraries with Flask app
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from Controllers.cli_controllers import db_commands
    app.register_blueprint(db_commands)
    
    from Controllers.auth_controller import player_bp
    app.register_blueprint(player_bp)\
    
    from Controllers.score_controller import goal_bp
    app.register_blueprint(goal_bp)
    
    return app
