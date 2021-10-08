from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

class RegistrationOfficeSchema(Schema):
    """
    Acts as the abstraction layer between the registration_office 
    table and user. This class allows us to control what fields 
    to accept from/sent back to the user.

    Important Attributes
    --------------------
    id: (Required) 
        Primary key in the table.
    Meta: (Required) 
        Class specifies metadata to be sent back to the user.

        Meta Attributes
        ---------------
        type_: (Required) 
            This is required in the Meta Class
        self_view:
            URL endpoint to an individual registration_office
        self_view_kwargs:
            Fields for self_view to pass to URL
        self_view_many:
            URL endpoint to all registration_office
    """

    class Meta:
        type_ = 'registration_office'
        self_view = 'registration_office_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'registration_office_many'

    id = fields.Integer()
    ngo_id =  fields.Str(required=True)
    registered_with = fields.Str()
    date = fields.Date()
    address = fields.Str()
    latitude = fields.Decimal()
    longitude = fields.Decimal()

    