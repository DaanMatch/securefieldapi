from api import api
from resource_managers import *


# Format: api.route(<Resource manager>, <endpoint name>, <url_1>, <url_2>, ...)

# Provides GET and POST to /field_data
api.route(FieldDataMany, 'field_data_many', '/field_data')

# Provides GET, PATCH, and DELETE to /field_data/<str:id>
api.route(FieldDataOne, 'field_data_one', '/field_data/<string:id>')

# Provides GET and POST to /daanmatch_ngos
api.route(DaanmatchNgoMany, 'daanmatch_ngo_many', '/daanmatch_ngos')

# Provides GET, PATCH, and DELETE to /daanmatch_ngo/<int:id>
api.route(DaanmatchNgoOne, 'daanmatch_ngo_one', '/daanmatch_ngo/<int:id>')

# Provides GET, POST, PATCH, and DELETE to 
# /daanmatch_ngo/<int:id>/relationships/registration_number
api.route(DaanmatchNgoRegistrationNumber, 
    'daanmatch_ngo_registration_number', 
    '/daanmatch_ngo/<int:id>/relationships/registration_number')

# Provides GET and POST to /registration_numbers
api.route(RegistrationNumberMany, 'registration_number_many', 
    '/registration_numbers')

# Provides GET, PATCH, and DELETE to /registration_number/<int:id>
api.route(RegistrationNumberOne, 'registration_number_one', 
    '/registration_number/<int:id>')

# Provides GET, POST, PATCH, and DELETE to 
# /registration_number/<int:id>/relationships/registration_office
api.route(RegistrationNumberRegistrationOffice, 
    'registration_number_registration_office', 
    '/registration_number/<int:id>/relationships/registration_office')
    
# Provides GET and POST to /registration_offices
api.route(RegistrationOfficeMany, 'registration_office_many', 
    '/registration_offices')

# Provides GET, PATCH, and DELETE to /registration_office/<int:id>
api.route(RegistrationOfficeOne, 'registration_office_one', 
    '/registration_office/<int:id>')









