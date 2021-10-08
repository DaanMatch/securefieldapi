from db import db

class Partnership(db.Model):
    """
    Defines the partnership table schema. All db.Column 
    attributes represent a column in the table. Tuples represent a 
    relationship between two NGOs.
    ...

    Important Attributes
    --------------------
    dummy:
        Primary key to satisfy ORM. Not in the actual database.
    ngo_id: 
        Foreign key for daanmatch_ngo.id.
    partner_id:
        Foreign key for daanmatch_ngo.id.
    daanmatch_ngo:
        Establish many-to-one relationship between daanmatch_ngo.id
        and partnership.ngo_id.
    daanmatch_ngo_partner:
        Establish many-to-one relationship between daanmatch_ngo.id
        and partnership.partner_id.
    """
    dummy = db.Column(db.Integer, primary_key = True)
    ngo_id =  db.Column(db.Integer, db.ForeignKey('daanmatch_ngo.id'), 
        nullable = False)
    partner_id =  db.Column(db.Integer, db.ForeignKey('daanmatch_ngo.id'), 
        nullable = False)
    relationship = db.Column(db.String)
    sector_id = db.Column(db.Integer)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        foreign_keys=[ngo_id],
        backref=db.backref('partnership_self', uselist = True))

    daanmatch_ngo_partner = db.relationship('DaanmatchNgo', 
        foreign_keys=[partner_id],  
        backref=db.backref('partnership', uselist = True))