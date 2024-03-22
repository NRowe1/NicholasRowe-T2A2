from flask import Blueprint

from init import db, bcrypt
from models.team import Team  # Import Team model here

from models.player import Player
from models.score import Score

db_commands = Blueprint('db', __name__)

db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")

from sqlalchemy import text

@db_commands.cli.command('drop')
def drop_tables():
    # Drop Score table first
    db.session.execute(text('DROP TABLE IF EXISTS score CASCADE'))
    # Then drop Player table
    db.session.execute(text('DROP TABLE IF EXISTS player CASCADE'))
    db.session.commit()
    print("Tables dropped")


@db_commands.cli.command('seed')
def seed_tables():
    players = [  
        Player(  
            first_name="Charlie",
            last_name="Cameron",
            position="Forward",
            jersey_number=23
        )
    ]

    db.session.add_all(players)  

    scores = [
        Score(
            goals=5,
            points=2,
            player=players[0]
        )
    ]
    db.session.add_all(scores)
    db.session.commit()
    team = [
        Team(
            team_name="Brisbane Lions"
        )
    ]
    
    db.session.add_all(team)
    db.session.commit()

    print("Tables seeded")