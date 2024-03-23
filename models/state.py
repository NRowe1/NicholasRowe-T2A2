from init import db, ma

class States(db.Model):
    __tablename__ = "state"  

    state_id = db.Column(db.Integer, primary_key=True)
    states_name = db.Column(db.String)  # Corrected column name from state_name to states_name

    team = db.relationship('Team', back_populates='state')


class StateSchema(ma.Schema):
    class Meta:
        fields = ('state_id', "state_name")
        model = States
