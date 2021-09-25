from flask_rest_jsonapi import ResourceList

from db import db
from schemas import RegistrationOfficeSchema
from models import RegistrationOffice

class RegistrationOfficeMany(ResourceList):
    schema = RegistrationOfficeSchema
    data_layer = {'session': db.session,
                  'model': RegistrationOffice}