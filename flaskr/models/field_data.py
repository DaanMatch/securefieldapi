from db import db
#from utils.sdg import SDG

class FieldData(db.Model):
    """
    Defines the Field Data table schema. All db.Column attributes 
    represent a column in the table.
    
    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Name of the user
    recorded_by:
        FK from member table
    date:

    address:

    latitude:

    longitude:

    title:

    comment:

    photo:

    sector_id:
    
    sdg:

    """
    
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.ngo_id'), 
        unique=True, nullable=False)
    recorded_by = db.Column(db.CHAR, db.ForeignKey('member.id'), 
        unique=True, nullable=False)
    date = db.Column(db.DATETIME) # Check
    address = db.Column(db.String)
    latitude = db.Column(db.FLOAT)
    longitude = db.Column(db.FLOAT)
    title = db.Column(db.String)    #Enum?
    comment = db.Column(db.String)
    photo = db.Column(db.String)
    sector_id = db.Column(db.CHAR)
    sdg = db.Column(db.CHAR)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('operation', uselist = False))
    member = db.relationship('Member', 
        backref=db.backref('operation', uselist = False))