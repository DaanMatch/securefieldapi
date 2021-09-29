from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import ActivitySchema
from models import Activity

class ActivityOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for activity.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = ActivitySchema
    data_layer = {'session': db.session,
                  'model': Activity}