from db import db

class RegistrationOffice(db.Model):
    """
    Defines the registration_number table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Unique and non-null. This is also the foreign key for the 
        registration_number table.
    registration_number:
        Establish one-to-one relationship between registration_office 
        and registration_number.
    """
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