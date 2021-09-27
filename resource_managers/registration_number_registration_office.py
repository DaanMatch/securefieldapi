from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import RegistrationNumberSchema
from models import RegistrationNumber

class RegistrationNumberRegistrationOffice(ResourceRelationship):
    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}