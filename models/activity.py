from db import db
from utils.sdg import SDG

class Activity(db.Model):
    """
    Defines the activity table schema. All db.Column attributes 
    represent a column in the table.
    ...

    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Not unique b/c an NGO's operation can have multiple activities.
        This is also the foreign key for the operation table.
    """
    id = db.Column(db.Integer, primary_key=True)
    ngo_id =  db.Column(db.CHAR, 
        nullable=False)
    name = db.Column(db.String)
    description = db.Column(db.String)
    date = db.Column(db.Date)
    issue = db.Column(db.Text)
    sdg = db.Column(db.Enum(SDG))
    beneficiaries = db.Column(db.Text)
    address = db.Column(db.String)
    state = db.Column(db.String)
    district = db.Column(db.String)
    city = db.Column(db.String)
    gram_panchayat = db.Column(db.String)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)