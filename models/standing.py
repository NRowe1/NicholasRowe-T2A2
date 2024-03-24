# from init import db, ma

# class Standing(db.Model):
#     __tablename__ = "standing"

#     standing_id = db.Column(db.Integer, primary_key=True)
#     wins = db.Column(db.Integer)
#     losses = db.Column(db.Integer)
#     ties = db.Column(db.Integer)
#     points = db.Column(db.Integer)

#     # Foreign key to relate standings to players
#     team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'), nullable=False)
    
#     # Establish the relationship with the Player model
#     team = db.relationship('Team', back_populates='standing')

# class StandingSchema(ma.Schema):
#     class Meta:
#         fields = ('standing_id', 'wins', 'losses', 'ties', 'points', 'team_id')
#         model = Standing
