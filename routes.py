from api import api
from resource_managers import *


# Format: api.route(<Resource manager>, <endpoint name>, <url_1>, <url_2>, ...)
api.route(RegistrationOfficeMany, 'registration_office_many', '/registration_offices')
api.route(RegistrationOfficeOne, 'registration_office_one', '/registration_office/<int:id>')
api.route(RegistrationNumberMany, 'registration_number_many', '/registration_numbers')
api.route(RegistrationNumberOne, 'registration_number_one', '/registration_number/<int:id>')
api.route(RegistrationOfficeRegistrationNumber, 
    'registration_office_registration_numbers', 
    '/registration_office/<int:id>/relationships/registration_numbers')
api.route(ActivityMany, 'activity_many', '/activities')
api.route(ActivityOne, 'activity_one', '/activity/<int:id>')







