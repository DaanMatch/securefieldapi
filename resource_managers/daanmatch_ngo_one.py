from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import DaanmatchNgoSchema
from models import DaanmatchNgo

class DaanmatchNgoOne(ResourceDetail):
    schema = DaanmatchNgoSchema
    data_layer = {'session': db.session,
                  'model': DaanmatchNgo}