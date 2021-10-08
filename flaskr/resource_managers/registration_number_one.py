from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import RegistrationNumberSchema
from models import RegistrationNumber

class RegistrationNumberOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for registration_number.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}