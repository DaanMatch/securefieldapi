from db import db

class RegistrationNumber(db.Model):
    """
    Defines the registration_number table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    ngo_id: 
        Primary key in the table. This is also the foreign key for the 
        daanmatch_ngo table.
    rn_12A_no: 
    rn_12A_regdate:
    rn_80G_no:
    rn_80G_regdate:
    rn_35AC_no:
    rn_35AC_regdate:
        These attrs are preceded w/ rn_ because variable names cannot 
        start w/ number.
    daanmatch_ngo:
        Establish one-to-one relationship between daanmatch_ngo 
        and registration_number.
    """
    ngo_id =  db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.id'), 
        primary_key=True)
    pan_no = db.Column(db.CHAR)
    pan_regdate = db.Column(db.Date)
    fcra_no = db.Column(db.CHAR)
    fcra_regdate = db.Column(db.Date)
    rn_12A_no = db.Column("12A_no", db.CHAR)
    rn_12A_regdate = db.Column("12A_regdate", db.Date)
    rn_80G_no = db.Column("80G_no", db.CHAR)
    rn_80G_regdate = db.Column("80G_regdate", db.Date)
    rn_35AC_no = db.Column("35AC_no", db.CHAR)
    rn_35AC_regdate = db.Column("35AC_regdate", db.Date)

    daanmatch_ngo = db.relationship('DaanmatchNgo', 
        backref=db.backref('registration_number', uselist = False))
