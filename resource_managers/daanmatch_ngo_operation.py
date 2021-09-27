from flask_rest_jsonapi import ResourceRelationship

from db import db
from schemas import DaanmatchNgoSchema
from models import DaanmatchNgo

class DaanmatchNgoOperation(ResourceRelationship):
    schema = DaanmatchNgoSchema
    data_layer = {'session': db.session,
                  'model': DaanmatchNgo}