from db import db

class District(db.Model):
    """
    Defines the district table schema. All db.Column 
    attributes represent a column in the table.
    ...

    Important Attributes
    --------------------
    id: 
        Primary key for the table.
    """
    id =  db.Column(db.CHAR,  primary_key=True)
    name = db.Column(db.String)
