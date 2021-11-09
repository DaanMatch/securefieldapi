from sqlalchemy.orm.exc import NoResultFound
from flask_rest_jsonapi import ResourceDetail
from flask_rest_jsonapi.exceptions import ObjectNotFound

from db import db
from schemas import FieldDataSchema
from models import FieldData
from auth.token_required import token_required
from auth.check_ids_match import check_member_ids_match
from limiter import limiter

class FieldDataOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for field_data. This manager only handles GET and 
    PATCH.
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
        Raises error if no field_data w/ provided id and deleted=False
        Also ensures that the member id matches recorded_by.
        """
        if view_kwargs.get('id') is not None:
            try: # try to get field data w/ id and deleted=False
                field_data = self.session.query(FieldData).filter_by(id=view_kwargs['id'], deleted=False).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'},
                                     "Field data: {} not found".format(view_kwargs['id']))
            
            # If the field_data.recorded_by != member_id in token, raise exception
            check_member_ids_match(field_data.recorded_by)

    def before_update_object(self, obj, data, view_kwargs):
        """
        Raises error if no field_data w/ provided id and deleted=False.
        Also ensures that the member id matches recorded_by.
        """
        if view_kwargs.get('id') is not None:
            try: # try to get field data w/ id and deleted=False
                field_data = self.session.query(FieldData).filter_by(id=view_kwargs['id'], deleted=False).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'},
                                     "Field data: {} not found".format(view_kwargs['id']))

            # If the field_data.recorded_by != member_id in token, raise exception
            check_member_ids_match(field_data.recorded_by)


    schema = FieldDataSchema
    data_layer = {'session': db.session,
                  'model': FieldData,
                  'methods': {'before_get_object': before_get_object,
                              'before_update_object': before_update_object}}
    methods = ['GET', 'PATCH']
    decorators = (
        token_required, 
        limiter.limit("5/second;30/minute"), 
    )