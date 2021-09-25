from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import RegistrationOfficeSchema
from models import RegistrationOffice

class RegistrationOfficeOne(ResourceDetail):
    schema = RegistrationOfficeSchema
    data_layer = {'session': db.session,
                  'model': RegistrationOffice}