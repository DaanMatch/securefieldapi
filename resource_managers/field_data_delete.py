from sqlalchemy.orm.exc import NoResultFound
from flask_rest_jsonapi import ResourceDetail
from flask_rest_jsonapi.exceptions import ObjectNotFound

from db import db
from schemas import FieldDataDeleteSchema
from models import FieldData
from auth.check_ids_match import check_member_ids_match
from auth.token_required import token_required
from limiter import limiter

class FieldDataDelete(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for field_data. This manager sets the deleted attr
    of field_data to True, thus only PATCH is implemented.
    ...

    Attributes
    ----------
    before_update_object:
        Custom validation before calling the PATCH method
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """
    def before_update_object(self, obj, data, view_kwargs):
        """
        Raises error if no field_data w/ provided id and deleted=False
        """
        if view_kwargs.get('id') is not None:
            try: # try to get field data w/ id and deleted=False
                field_data = self.session.query(FieldData).filter_by(id=view_kwargs['id'], deleted=False).one()
                data['deleted'] = True
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'},
                                     "Field data: {} not found".format(view_kwargs['id']))
            # If the field_data.recorded_by != member_id in token, raise exception
            check_member_ids_match(field_data.recorded_by)


    schema = FieldDataDeleteSchema
    data_layer = {'session': db.session,
                  'model': FieldData,
                  'methods': {'before_update_object': before_update_object}}
    methods = ['PATCH']
    decorators = (
        token_required, 
        limiter.limit("5/second;30/minute"), 
    )