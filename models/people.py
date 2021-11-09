from setup.db import db

class People(db.Model):
    """
    Defines the people table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    ngo_id: 
        The ngo this person is related to. Foreign key to daanmatch_ngo.id.
    member_id: 
        The person's member id. Foreign key to member.id.
    daanmatch_ngo:
        Establish one-to-many relationship between daanmatch_ngo 
        and people.
    member:
        Establish one-to-one relationship between finance 
        and daanmatch_ngo.
    """
    id = db.Column(db.Integer, primary_key = True)
    ngo_id =  db.Column(db.Integer, db.ForeignKey('daanmatch_ngo.id'))
    member_id =  db.Column(db.Integer, db.ForeignKey('member.id'))
    designation = db.Column(db.String)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('people', uselist = False))
    member = db.relationship('Member', 
        backref=db.backref('people', uselist = False))