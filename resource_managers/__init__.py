"""
General format for each ResourceManager:
...

Inherits from one of:
    ResourceList: Provides GET, POST
    ResourceDetail: Provides GET, PATCH, DELETE
    ResourceRelationship: Provides GET, POST, PATCH, DELETE

class ResourceManager(Resource_________):

    # The schema for the resource being managed
    schema = ResourceSchema

    # Implements CRUD interface for objects and relationships.
    data_layer = {'session': db.session,    # Required attr
                  'model': ResourceModel}   # Required attr
"""

from .field_data_delete import *
from .field_data_many import *
from .field_data_one import *
from .member_one import *