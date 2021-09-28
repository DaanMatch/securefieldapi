from db import db
from utils.sdg import SDG

class Operation(db.Model):
    """
    Defines the operation table schema. All db.Column attributes 
    represent a column in the table.
    ...

    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Unique and non-null. This is also the foreign key for the 
        daanmatch_ngo table.
    sdgs: 
        SDG class currently not implemented. This field is likely to be 
        removed in the future.
    daanmatch_ngo:
        Establish one-to-one relationship between operation and 
        daanmatch_ngo.
    """
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.ngo_id'), 
        unique=True, nullable=False)
    issues = db.Column(db.String)
    sdgs = db.Column(db.Enum(SDG))
    states = db.Column(db.String)
    cities = db.Column(db.String)
    district = db.Column(db.String)
    gram_panchayats = db.Column(db.String)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('operation', uselist = False))