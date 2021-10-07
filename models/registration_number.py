from db import db

class RegistrationNumber(db.Model):
    """
    Defines the registration_number table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Unique and non-null. This is also the foreign key for the 
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
        Establish one-to-one relationship between registration_number 
        and daanmatch_ngo.
    """
    id = db.Column(db.Integer, primary_key=True)
    ngo_id =  db.Column(db.CHAR, db.ForeignKey('daanmatch_ngo.ngo_id'), 
        unique=True, nullable=False)
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
