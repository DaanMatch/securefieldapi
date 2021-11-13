from setup.api import api
from setup.app import app
from auth.login import login_member
from resource_managers import *
from utils.limiter import limiter


# login route, could not get to work w/ flask_rest_jsonapi extention
@limiter.limit("10/30minutes")
@app.route('/login', methods=['GET', 'POST']) 
def login():
    return login_member()


# Format: api.route(<Resource manager>, <endpoint name>, <url_1>, <url_2>, ...)

# Provides PATCH to /field_data/<int:id>
api.route(FieldDataDelete, 'field_data_delete', '/field_data/<int:id>/delete')

# Provides GET to /member/<int:id>/field_data and POST to /field_data
api.route(FieldDataMany, 'field_data_many', 
    '/field_data', '/member/<int:id>/field_data')

# Provides GET to /ngo/<int:ngo_id>/field_data/
# Must have "OM" designation to access this route
api.route(FieldDataNgoMany, 'field_data_ngo_many', 
    '/field_data_ngo', '/ngo/<int:id>/field_data')

# Provides GET, PATCH to /field_data/<int:id>
api.route(FieldDataOne, 'field_data_one', '/field_data/<int:id>')

# Provides GET, PATCH to /member/<int:id>
api.route(MemberOne, 'member_one', '/member/<int:id>')












