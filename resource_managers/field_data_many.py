from flask_rest_jsonapi import ResourceList

from db import db
from schemas import FieldDataSchema
from models import FieldData

class FieldDataMany(ResourceList):
    """
    Inheriting from ResourceList creates GET (multiple) and POST 
    methods for field_data.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = FieldDataSchema
    data_layer = {'session': db.session,
                  'model': FieldData}