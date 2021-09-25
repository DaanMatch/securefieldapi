from flask_rest_jsonapi import ResourceList

from db import db
from schemas import ActivitySchema
from models import Activity

class ActivityMany(ResourceList):
    schema = ActivitySchema
    data_layer = {'session': db.session,
                  'model': Activity}