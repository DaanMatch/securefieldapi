from api import api
from resource_managers import *


# Format: api.route(<Resource manager>, <endpoint name>, <url_1>, <url_2>, ...)


# Provides GET and POST to 
# /member/<int:id>/field_data and /field_data
api.route(FieldDataMany, 'field_data_many', 
    '/member/<int:id>/field_data')

# Provides GET, PATCH, and DELETE to /field_data/<int:id>
api.route(FieldDataOne, 'field_data_one', '/field_data/<int:id>')

# Provides GET, PATCH to /member/<int:id>
api.route(MemberOne, 'member_one', '/member/<int:id>')



# FOR TESTING ONLY, TODO: DELETE THIS LATER
# Provides POST to /member
api.route(MemberMany, 'member_many', '/member')










