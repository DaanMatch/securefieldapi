from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

class RegistrationOfficeSchema(Schema):
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

    