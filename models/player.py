from init import db, ma
from marshmallow import fields

class Player(db.Model):
    __tablename__ = "player"

    player_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    position = db.Column(db.String)
    jersey_number = db.Column(db.Integer)

    score = db.relationship('Score', back_populates='player', cascade='all, delete')  

    # Define the foreign key relationship
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))  # Corrected foreign key reference

    # Adjust the backref name to avoid conflict
    team = db.relationship('Team', back_populates='players')

class PlayerSchema(ma.Schema):
    Score = fields.List(fields.Nested('ScoreSchema', exclude=['player']))

    class Meta:
        fields = ('player_id','first_name', 'last_name', 'position', 'jersey_number')
        model = Player

