import os
from flask import Flask
from flask_migrate import Migrate
from init import db  # Import your Flask application instance and database

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")

# Initialize Flask-Migrate
migrate = Migrate(app, db)
