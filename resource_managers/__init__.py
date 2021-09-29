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

from .activity_many import *
from .activity_one import *

from .daanmatch_ngo_many import *
from .daanmatch_ngo_one import *
from .daanmatch_ngo_operation import *
from .daanmatch_ngo_registration_number import *

from .operation_one import *
from .operation_many import *
from .operation_activities import *

from .registration_number_many import *
from .registration_number_one import *
from .registration_number_registration_office import *

from .registration_office_many import *
from .registration_office_one import *
