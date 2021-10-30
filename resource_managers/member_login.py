from flask_rest_jsonapi import ResourceList
from flask_rest_jsonapi.resource import ResourceDetail

from db import db
from auth.login import login_member
from schemas import MemberSchema
from models import Member


class MemberLogin(ResourceDetail):
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
    def query(self, view_kwargs):
        return login_member()


    schema = MemberSchema
    data_layer = {'session': db.session,
                  'model': Member,
                  'methods': {'query': query}}
    methods = ['GET']