from flask_rest_jsonapi import ResourceList

from db import db
from schemas import RegistrationNumberSchema
from models import RegistrationNumber

class RegistrationNumberMany(ResourceList):
    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}