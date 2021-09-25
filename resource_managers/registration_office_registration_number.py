from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import RegistrationOfficeSchema
from models import RegistrationOffice

class RegistrationOfficeRegistrationNumber(ResourceRelationship):
    schema = RegistrationOfficeSchema
    data_layer = {'session': db.session,
                  'model': RegistrationOffice}