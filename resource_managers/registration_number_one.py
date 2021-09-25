from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import RegistrationNumberSchema
from models import RegistrationNumber

class RegistrationNumberOne(ResourceDetail):
    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}