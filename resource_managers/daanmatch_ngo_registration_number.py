from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import DaanmatchNgoSchema
from models import DaanmatchNgo

class DaanmatchNgoRegistrationNumber(ResourceRelationship):
    """
    Inheriting from ResourceRelationship creates GET, POST, PATCH, and 
    DELETE methods for a daanmatch_ngo's registration_number.
    ...

    Attributes
    ----------
    schema:
        The schema for the resource being managed
    data_layer:
        Implements CRUD interface for objects and relationships. 
        session and model are required params.
    """

    schema = DaanmatchNgoSchema
    data_layer = {'session': db.session,
                  'model': DaanmatchNgo}