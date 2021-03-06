"""
General format for each model:
...

# All models inherit from db.Model. (db is a SQLAlchemy() object)
# TableNames are converted from UpperCamelCase to snake_case in the db.

class TableName(db.Model): 

    # Table Attributes:
    id = db.Column(db.Integer, primary_key=True)
    ngo_id = db.Column(db.CHAR)
    attr_1 = ...

    # Relationships: (Usually only 1 parent)
    parent_1 = db.relationship(...)
    parent_2 = ...

"""

from .daanmatch_ngo import *
from .field_data import *
from .member import *
from .people import *
