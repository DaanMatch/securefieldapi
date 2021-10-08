from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import DaanmatchNgoSchema
from models import DaanmatchNgo

class DaanmatchNgoOne(ResourceDetail):
    """
    Inheriting from ResourceDetail creates GET, PATCH, and DELETE 
    methods for daanmatch_ngo.
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