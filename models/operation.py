from db import db
from utils.sdg import SDG

class Operation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.ngo_id'))
    issues = db.Column(db.String)
    sdgs = db.Column(db.Enum(SDG))
    states = db.Column(db.String)
    cities = db.Column(db.String)
    district = db.Column(db.String)
    gram_panchayats = db.Column(db.String)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('operation', uselist = False))