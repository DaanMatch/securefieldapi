from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import OperationSchema
from models import Operation

class OperationOne(ResourceDetail):
    schema = OperationSchema
    data_layer = {'session': db.session,
                  'model': Operation}