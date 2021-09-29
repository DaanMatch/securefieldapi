from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import RegistrationOfficeSchema
from models import RegistrationOffice

class RegistrationOfficeOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for registration_office.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = RegistrationOfficeSchema
    data_layer = {'session': db.session,
                  'model': RegistrationOffice}