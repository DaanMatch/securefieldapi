from setup.db import db

class FieldData(db.Model):
    """
    Defines the field_data table schema. All db.Column attributes 
    represent a column in the table.
    ...

    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Not unique b/c an NGO might can have many field_data.
        This is also the foreign key for the daanmatch_ngo table.
    sdg:
        Sustainable development goals. 
        This field might be removed later on.

    daanmatch_ngo:
        Creates a relationship between daanmatch_ngo and field_data
    member:
        Creates a relationship between member and field_data
    """
    
    id = db.Column(db.Integer, primary_key=True)
    ngo_id =  db.Column(db.Integer, db.ForeignKey('daanmatch_ngo.id'),
        nullable=False)
    recorded_by = db.Column(db.Integer, db.ForeignKey('member.id'))
    date = db.Column(db.Date)
    address = db.Column(db.Text)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)
    title = db.Column(db.String)
    comment = db.Column(db.Text)
    media = db.Column(db.Text)
    media_type = db.Column(db.Text)
    sector_id = db.Column(db.Integer)
    sdg = db.Column(db.CHAR)
    deleted = db.Column(db.Boolean)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('field_data', uselist = False))

    member = db.relationship('Member', 
        backref=db.backref('field_data', uselist = True))
