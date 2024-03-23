from init import db, ma
from marshmallow import fields

class Games(db.Model):
    __tablename__ = "games"

    games_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    location = db.Column(db.String)

    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))  # Corrected foreign key reference
    team = db.relationship('Team', back_populates='games')


class GamesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('games_id', 'date', 'time', 'location', 'team_id')
        model = Games
