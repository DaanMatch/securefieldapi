from models.activity import Activity
from schemas.activity_schema import ActivitySchema
from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import OperationSchema
from models import Operation

class OperationActivities(ResourceRelationship):
    """
    Inheriting from ResourceRelationship creates GET, POST, PATCH, and 
    DELETE methods for an operation's activities.
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