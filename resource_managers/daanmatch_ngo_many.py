from flask_rest_jsonapi import ResourceList

from db import db
from schemas import DaanmatchNgoSchema
from models import DaanmatchNgo

class DaanmatchNgoMany(ResourceList):
    schema = DaanmatchNgoSchema
    data_layer = {'session': db.session,
                  'model': DaanmatchNgo}