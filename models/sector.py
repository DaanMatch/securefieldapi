from db import db

class Sector(db.Model):
    """
    Defines the sector table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    id: 
        Primary key for the table.
    """
    id =  db.Column(db.CHAR,  primary_key=True)
    description = db.Column(db.String)
