from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import MemberSchema
from models import Member

class MemberFieldData(ResourceRelationship):
    """
    Inheriting from ResourceRelationship creates POST, GET, PATCH, and DELETE 
    methods for field_data. 
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    methods:
        Selects which methods are available 
    """

    schema = MemberSchema
    data_layer = {'session': db.session,
                  'model': Member}
    methods = ['POST', 'GET']