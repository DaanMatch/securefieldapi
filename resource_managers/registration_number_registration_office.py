from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import RegistrationNumberSchema
from models import RegistrationNumber

class RegistrationNumberRegistrationOffice(ResourceRelationship):
    """
    Inheriting from ResourceRelationship creates GET, POST, PATCH, and 
    DELETE methods for a registration_numbers's registration_office.
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