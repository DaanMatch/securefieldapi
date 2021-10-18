from db import db

class Member(db.Model):
    """
    Defines the member schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    id: 
        Primary key for the table.
    password:
        For auth. This is the only field that the user creates.
    """
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mobile = db.Column(db.String)
    email = db.Column(db.String)
    data_manager = db.Column(db.String)
    password = db.Column(db.String)