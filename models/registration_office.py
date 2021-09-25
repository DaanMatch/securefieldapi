from db import db

class RegistrationOffice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_id =  db.Column(db.CHAR)
    registered_with = db.Column(db.String)
    date = db.Column(db.Date)
    address = db.Column(db.String)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)