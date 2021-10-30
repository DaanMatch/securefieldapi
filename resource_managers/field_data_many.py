from sqlalchemy.orm.exc import NoResultFound
from flask_rest_jsonapi import ResourceList
from flask_rest_jsonapi.exceptions import ObjectNotFound

from db import db
from schemas import FieldDataSchema
from models import FieldData, Member
from auth.token_required import token_required

class FieldDataMany(ResourceList):
    """
    Inheriting from ResourceList creates GET (multiple) and POST 
    methods for field_data.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    query:
        Custom query function replaces the default inherited by 
        ResourceList. Allows members to get their associated
        field_data.
    before_create_object:
        Allow field_data.recorded_by to be autofilled when posting
        from /member/<int:id>/field_data
    """
    def query(self, view_kwargs):
        query_ = self.session.query(FieldData)

        # Filter all field_data corresponding to member.id
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Member).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Member: {} not found".format(view_kwargs['id']))
            else: # Join Member.id w/ FieldData.recorded_by (foreign key)
                query_ = query_.join(Member).filter(Member.id == view_kwargs['id'])
        
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            member = self.session.query(Member).filter_by(id=view_kwargs['id']).one()
            data['recorded_by'] = member.id


    schema = FieldDataSchema
    data_layer = {'session': db.session,
                  'model': FieldData,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}
    decorators = (token_required,)