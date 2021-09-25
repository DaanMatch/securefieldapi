from flask_rest_jsonapi import ResourceDetail

from db import db
from schemas import ActivitySchema
from models import Activity

class ActivityOne(ResourceDetail):
    schema = ActivitySchema
    data_layer = {'session': db.session,
                  'model': Activity}