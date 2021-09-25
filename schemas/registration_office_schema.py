from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

class RegistrationOfficeSchema(Schema):
    class Meta:
        type_ = 'registration_office'
        self_view = 'registration_office_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'registration_office_many'

    id = fields.Integer()
    ngo_id =  fields.Str()
    registered_with = fields.Str()
    date = fields.Date()
    address = fields.Str()
    latitude = fields.Decimal()
    longitude = fields.Decimal()

    registration_numbers = Relationship(self_view = 'registration_office_registration_numbers',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'registration_number_many',
        many = False,
        schema = 'RegistrationNumberSchema',
        type_ = 'registration_number')