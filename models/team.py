from init import db, ma

class Team(db.Model):
    __tablename__ = "team"

    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String)
    
    # Adjust the backref name to avoid conflict
    players = db.relationship('Player', back_populates='team')

class TeamSchema(ma.Schema):
    class Meta:
        fields = ('team_id', 'team_name')
        model = Team