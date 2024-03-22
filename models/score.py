from init import db, ma
from marshmallow import fields

class Score(db.Model):
    __tablename__ = "goals"  # Corrected table name to 'goals'

    score_id = db.Column(db.Integer, primary_key=True)
    goals = db.Column(db.Integer)
    points = db.Column(db.Integer)

    player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'), nullable=False)
    player = db.relationship('Player', back_populates='score')


class ScoreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ('score_id','goals', 'points')
        model = Score