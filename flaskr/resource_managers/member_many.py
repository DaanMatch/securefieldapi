from flask_rest_jsonapi import ResourceList

from db import db
from schemas import MemberSchema
from models import Member

class MemberMany(ResourceList):
    """
    Inheriting from ResourceList creates GET (multiple) and POST 
    methods for field_data. We only need POST for now. 
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
    methods = ['POST']