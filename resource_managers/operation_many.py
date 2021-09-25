from flask_rest_jsonapi import ResourceList

from db import db
from schemas import OperationSchema
from models import Operation

class OperationMany(ResourceList):
    schema = OperationSchema
    data_layer = {'session': db.session,
                  'model': Operation}