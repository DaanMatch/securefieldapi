from db import db

class DaanmatchNgo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.CHAR)
    name = db.Column(db.String)
    description = db.Column(db.Text)
    majoracivity_description = db.Column(db.Text)
    type = db.Column(db.String)
    last_updated = db.Column(db.DateTime)
    address = db.Column(db.String)
    mobile = db.Column(db.String)
    email = db.Column(db.String)
    fax = db.Column(db.String)
    website = db.Column(db.String)
    facebook = db.Column(db.String)
    twitter = db.Column(db.String)
    fulltime_staff = db.Column(db.Integer)
    parttime_staff = db.Column(db.Integer)
    volunteers = db.Column(db.Integer)
    partner_ids = db.Column(db.CHAR)

    