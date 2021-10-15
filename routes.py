from api import api
from resource_managers import *


# Format: api.route(<Resource manager>, <endpoint name>, <url_1>, <url_2>, ...)

# TODO: member/id/field_data url needs to only get data from member.id
# Provides GET and POST to /field_data
api.route(FieldDataMany, 'field_data_many', 
    '/field_data', '/member/<int:id>/field_data')

# Provides GET, PATCH, and DELETE to /field_data/<int:id>
api.route(FieldDataOne, 'field_data_one', '/field_data/<int:id>')

# Provides GET, PATCH to /member/<int:id>
api.route(MemberOne, 'member_one', '/member/<int:id>')


# Might delete this, unsure
# Provides GET, POST to /member/<int:id>/field_data
# api.route(MemberFieldData, 'member_field_data', '/member/<int:id>/field_data')


# FOR TESTING ONLY, TODO: DELETE THIS LATER
# Provides POST to /member
api.route(MemberMany, 'member_many', '/member')










