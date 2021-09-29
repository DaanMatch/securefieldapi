from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import OperationSchema
from models import Operation

class OperationOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for operation.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = OperationSchema
    data_layer = {'session': db.session,
                  'model': Operation}