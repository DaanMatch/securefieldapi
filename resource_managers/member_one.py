from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import MemberSchema
from models import Member

class MemberOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for member. We only need GET and PATCH.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = MemberSchema
    data_layer = {'session': db.session,
                  'model': Member}
    methods = ['GET', 'PATCH']  