from db import db
from utils.sdg import SDG

class FieldData(db.Model):
    """
    Defines the field_data table schema. All db.Column attributes 
    represent a column in the table.
    ...

    Important Attributes
    --------------------
    id:
        Primary key in the table.
    ngo_id: 
        Not unique b/c an NGO's operation can have multiple activities.
        This is also the foreign key for the operation table.
    sdg:
        Sustainable development goals. SDG class must be implemented.
        This field might be removed later on.
    """
    id = db.Column(db.CHAR, primary_key=True)
    ngo_id =  db.Column(db.CHAR, 
        nullable=False)
    recorded_by = db.Column(db.Text)
    description = db.Column(db.Text)
    date = db.Column(db.Date)
    sector_id = db.Column(db.Text)
    sdg = db.Column(db.Enum(SDG))
    beneficiaries = db.Column(db.Text)
    address = db.Column(db.String)
    state_id = db.Column(db.String)
    district_id = db.Column(db.String)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)
    title = db.Column(db.String)
    comment = db.Column(db.Text)
    media = db.Column(db.Text)
    media_type = db.Column(db.Text)