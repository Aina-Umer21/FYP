from config import db

class MissionDataImages(db.Model):
    __tablename__ = "MissionDataImages"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_data_location_id = db.Column(db.Integer, db.ForeignKey("MissionDataLocation.id"))
    image_path = db.Column(db.String(300), nullable=False)
    validity = db.Column(db.Integer, nullable=False, default=1)

    missionDataLocation = db.relationship('MissionDataLocation', back_populates='missionDataImages')
