from db import db

class RegistrationNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ngo_id =  db.Column(db.CHAR)
    pan_no = db.Column(db.CHAR)
    pan_regdate = db.Column(db.Date)
    fcra_no = db.Column(db.CHAR)
    fcra_regdate = db.Column(db.Date)
    rn_12A_no = db.Column(db.CHAR)
    rn_12A_regdate = db.Column(db.Date)
    rn_80G_no = db.Column(db.CHAR)
    rn_80G_regdate = db.Column(db.Date)
    rn_35AC_no = db.Column(db.CHAR)
    rn_35AC_regdate = db.Column(db.Date)

    
