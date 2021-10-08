from db import db

class RegistrationOffice(db.Model):
    """
    Defines the registration_number table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    ngo_id: 
        Primary key for daanmatch_ngo.ig. This is also the foreign key 
        for the daanmatch_ngo table.
    daanmatch_ngo:
        Establish one-to-one relationship between daanmatch_ngo 
        and registration_office.
    """
    ngo_id =  db.Column(db.Integer, db.ForeignKey('daanmatch_ngo.id'), 
        primary_key=True)
    registered_with = db.Column(db.String)
    date = db.Column(db.Date)
    address = db.Column(db.String)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('registration_office', uselist = False))