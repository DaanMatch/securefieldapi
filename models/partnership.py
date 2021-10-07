from db import db

class Partnership(db.Model):
    """
    Defines the partnership table schema. All db.Column 
    attributes represent a column in the table. Tuples represent a 
    relationship between two NGOs.
    ...

    Important Attributes
    --------------------
    ngo_id: 
        Foreign key for daanmatch_ngo.id.
    partner_id:
        Foreign key for daanmatch_ngo.id.
    daanmatch_ngo:
        Establish many-to-one relationship between daanmatch_ngo.id
        and partnership.ngo_id.
    daanmatch_ngo_p:
        Establish many-to-one relationship between daanmatch_ngo.id
        and partnership.partner_id.
    """
    # TODO: Consider different implementation
    id = db.Column(db.Integer, primary_key = True)
    ngo_id =  db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.id'), 
        nullable = False)
    partner_id =  db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.id'), 
        nullable = False)
    relationship = db.Column(db.String)
    sector_id = db.Column(db.CHAR)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('partnership', uselist = True))

    daanmatch_ngo_p = db.relationship('DaanmatchNgo', 
        backref=db.backref('partnership', uselist = True))