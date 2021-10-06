from db import db
#from utils.sdg import SDG

class People(db.Model):
    """
    Defines the People table schema. All db.Column attributes 
    represent a column in the table.
    -> All people related to NGOs
    
    Important Attributes
    --------------------
    ngo_id:
        Primary key in the table. FK from daanmatch_ngo
    member_id: 
        Name of the user. FK from member
    designation:
        ** Need to ask**
    """
    
    #ngo_id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.ngo_id'), 
        unique=True, nullable=False)
    member_id = db.Column(db.CHAR, db.ForeignKey('member.id'), 
        unique=True, nullable=False)
    designation = db.Column(db.String)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('operation', uselist = False))
    member = db.relationship('Member', 
        backref=db.backref('operation', uselist = False))