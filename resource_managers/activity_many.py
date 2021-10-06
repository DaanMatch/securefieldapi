from flask_rest_jsonapi import ResourceList

from db import db
from schemas import ActivitySchema
from models import Activity

class ActivityMany(ResourceList):
    """
    Inheriting from ResourceList creates GET (multiple) and POST 
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