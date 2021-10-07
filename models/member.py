from db import db

class Member(db.Model):
    """
    Defines the finance member schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    id: 
        Primary key for the table.
    """
    id =  db.Column(db.CHAR, primary_key=True)
    mobile = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)