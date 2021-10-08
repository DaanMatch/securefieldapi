from db import db

class Finance(db.Model):
    """
    Defines the finance table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    ngo_id: 
        Primary key for the table.
    daanmatch_ngo:
        Establish one-to-one relationship between daanmatch_ngo 
        and finance.
    """
    ngo_id =  db.Column(db.Integer, db.ForeignKey('daanmatch_ngo.id'), 
        primary_key=True)
    annual_expenditure = db.Column(db.Float)
    total_funding_gap = db.Column(db.Float)
    total_funding_gap = db.Column(db.Integer)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('finance', uselist = False))