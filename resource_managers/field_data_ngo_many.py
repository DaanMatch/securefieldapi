from sqlalchemy.orm.exc import NoResultFound
from flask_rest_jsonapi import ResourceList
from flask_rest_jsonapi.exceptions import AccessDenied, ObjectNotFound
from flask import request
import jwt

from setup.db import db
from schemas import FieldDataSchema
from models import FieldData, DaanmatchNgo
from auth.token_required import token_required
from auth.get_roles import get_roles
from utils.limiter import limiter
from setup.config import SECRET_KEY


class FieldDataNgoMany(ResourceList):
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
    """
    def query(self, view_kwargs):
        """
        Gets all field_data for the user by matching view_kwargs['id']
        (the member id) with field_data.recorded_by (foreign key).
        """
        token = request.headers['x-access-tokens']
        token_data = jwt.decode(token, SECRET_KEY)
        member_id = token_data['member_id']

        query_ = self.session.query(FieldData).filter_by(deleted=False)
        
        roles_dict = get_roles(member_id)

        # Filter all field_data corresponding to member.id
        if view_kwargs.get('id') is not None:
            ngo_id = view_kwargs.get('id')

            # The member must be designated 'OM' for this NGO to access
            # all the NGO's field_data
            if ngo_id not in roles_dict or 'OM' not in roles_dict[ngo_id]:
                 raise AccessDenied(
                    {'parameter': 'id'}, 
                    "Member {} cannot access ngo {}'s field_data. They are not an OM for ngo {}.".format(
                        member_id, ngo_id, ngo_id
                    )
                )
            try:
                self.session.query(DaanmatchNgo).filter_by(id=ngo_id).one()
            except NoResultFound:
                raise ObjectNotFound(
                    {'parameter': 'id'}, 
                    "DaanmatchNgo: {} not found".format(ngo_id)
                )
            else: # Join Member.id w/ FieldData.recorded_by (foreign key) by default
                query_ = query_.join(DaanmatchNgo).filter(DaanmatchNgo.id == ngo_id)
        
        return query_


    schema = FieldDataSchema
    data_layer = {'session': db.session,
                  'model': FieldData,
                  'methods': {'query': query}}
    methods = ['GET']
    decorators = (
        token_required, 
        limiter.limit("5/second;30/minute"), 
    )
   