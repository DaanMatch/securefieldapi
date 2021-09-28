from db import db

class RegistrationOffice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_id =  db.Column(db.CHAR, db.ForeignKey('registration_number.ngo_id'), 
        unique=True, nullable=False)
    registered_with = db.Column(db.String)
    date = db.Column(db.Date)
    address = db.Column(db.String)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)

    registration_number = db.relationship('RegistrationNumber', 
        backref=db.backref('registration_office', uselist = False))