from sqlalchemy.orm.exc import NoResultFound
from flask_rest_jsonapi import ResourceList
from flask_rest_jsonapi.exceptions import AccessDenied, ObjectNotFound

from setup.db import db
from schemas import FieldDataSchema
from models import FieldData, Member
from auth.check_ids_match import check_member_ids_match
from auth.get_roles import get_roles
from auth.token_required import token_required
from utils.limiter import limiter


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
        """
        Gets all field_data for the user by matching view_kwargs['id']
        (the member id) with field_data.recorded_by (foreign key).
        
        Params
        ------
        view_kwargs:
            The args passed in the URL
        """
        query_ = self.session.query(FieldData).filter_by(deleted=False)

        # Filter all field_data corresponding to member.id
        if view_kwargs.get('id') is not None:
            # If the id != member_id in token, raise exception
            check_member_ids_match(view_kwargs['id'])

            try:
                self.session.query(Member).filter_by(id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound(
                    {'parameter': 'id'}, 
                    "Member: {} not found".format(view_kwargs['id'])
                )
            else: # Join Member.id w/ FieldData.recorded_by (foreign key) by default
                query_ = query_.join(Member).filter(Member.id == view_kwargs['id'])
        
        return query_


    def before_create_object(self, data, view_kwargs):
        """
        Automatically sets new field_data.recorded_by to appropriate 
        member id and sets field_data.deleted to False.
        Also ensures that the user has the proper designation.

        Params
        ------
        data:
            The data part of the request body
        view_kwargs:
            The args passed in the URL
        """
        if view_kwargs.get('id') is not None:
            # If the id != member_id in token, raise exception  
            check_member_ids_match(view_kwargs['id'])

            roles_dict = get_roles()
            ngo_id = data['ngo_id']
            # if not an DM for the ngo
            if ngo_id not in roles_dict or 'DM' not in roles_dict[ngo_id]:
                 raise AccessDenied(
                    {'parameter': 'id'}, 
                    "Member cannot create ngo {}'s field_data. They are not an DM for ngo {}.".format(
                        ngo_id, ngo_id
                    )
                )

            member = self.session.query(Member).filter_by(id=view_kwargs['id']).one()
            data['recorded_by'] = member.id
            data['deleted'] = False



    schema = FieldDataSchema
    data_layer = {'session': db.session,
                  'model': FieldData,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}
    decorators = (
        token_required, 
        limiter.limit("5/second;45/minute,300/hour"), 
    )