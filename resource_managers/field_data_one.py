from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import FieldDataSchema
from models import FieldData
from auth.token_required import token_required

class FieldDataOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for field_data. DELETE will eventually need to be replaced
    with some custom method for deleting field_data.
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
    decorators = (token_required,)