from models.activity import Activity
from schemas.activity_schema import ActivitySchema
from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import OperationSchema
from models import Operation

class OperationActivities(ResourceRelationship):
    schema = OperationSchema
    data_layer = {'session': db.session,
                  'model': Operation}