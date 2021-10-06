from db import db
#from utils.sdg import SDG

class Member(db.Model):
    """
    Defines the member table schema. All db.Column attributes 
    represent a column in the table.
    -> All people related to NGOs
    
    Important Attributes
    --------------------
    id:
        Primary key in the table.
    name: 
        Name of the user
    mobile: 
        Mobile number of the user
    email:
        Email address of the user
    mobile_id:
        The device id of the mobile the user is accessing from
    """
    
    id = db.Column(db.Integer, primary_key=True)
    # ngo_id = db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.ngo_id'), 
    #     unique=True, nullable=False)
    name = db.Column(db.String)
    mobile = db.Column(db.String)
    email = db.Column(db.String)
    mobile_id = db.Column(db.String)
    

    # daanmatch_ngo = db.relationship('DaanmatchNgo', 
    #     backref=db.backref('operation', uselist = False))