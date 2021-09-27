from api import api
from resource_managers import *


# Format: api.route(<Resource manager>, <endpoint name>, <url_1>, <url_2>, ...)
api.route(ActivityMany, 'activity_many', '/activities')
api.route(ActivityOne, 'activity_one', '/activity/<int:id>')

api.route(DaanmatchNgoMany, 'daanmatch_ngo_many', '/daanmatch_ngos')
api.route(DaanmatchNgoOne, 'daanmatch_ngo_one', '/daanmatch_ngo/<int:id>')
api.route(DaanmatchNgoOperation, 
    'daanmatch_ngo_operation', 
    '/daanmatch_ngo/<int:id>/relationships/operation')
api.route(DaanmatchNgoRegistrationNumber, 
    'daanmatch_ngo_registration_number', 
    '/daanmatch_ngo/<int:id>/relationships/registration_number')

api.route(OperationMany, 'operation_many', '/operations')
api.route(OperationOne, 'operation_one', '/operation/<int:id>')
api.route(OperationActivities, 'operation_activities', 
    '/operation/<int:id>/relationships/activities')

api.route(RegistrationNumberMany, 'registration_number_many', '/registration_numbers')
api.route(RegistrationNumberOne, 'registration_number_one', '/registration_number/<int:id>')
api.route(RegistrationNumberRegistrationOffice, 
    'registration_number_registration_office', 
    '/registration_number/<int:id>/relationships/registration_office')
    
api.route(RegistrationOfficeMany, 'registration_office_many', '/registration_offices')
api.route(RegistrationOfficeOne, 'registration_office_one', '/registration_office/<int:id>')









