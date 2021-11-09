from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import MemberSchema
from models import Member
from auth.token_required import token_required
from auth.check_ids_match import check_member_ids_match
from limiter import limiter

class MemberOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for member. We only need GET and PATCH.
    ...

    Attributes
    ----------
    before_get_object:
        Custom validation before calling the GET method
    before_update_object:
        Custom validation before calling the PATCH method
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """
    def before_get_object(self, view_kwargs):
        """
        Ensures that the member id matches recorded_by
        """
        # If the id != member_id in token, raise exception
        check_member_ids_match(view_kwargs['id'])

    def before_update_object(self, obj, data, view_kwargs):
        """
        Ensures that the member id matches recorded_by
        """
        # If the id != member_id in token, raise exception
        check_member_ids_match(view_kwargs['id'])

    schema = MemberSchema
    data_layer = {'session': db.session,
                  'model': Member,
                  'methods': {'before_get_object': before_get_object,
                              'before_update_object': before_update_object}}
    methods = ['GET', 'PATCH']  
    decorators = (
        token_required, 
        limiter.limit("5/second;30/minute"), 
    )