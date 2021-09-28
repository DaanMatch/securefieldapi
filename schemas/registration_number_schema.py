from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema


class RegistrationNumberSchema(Schema):
    class Meta:
        type_ = 'registration_number'
        self_view = 'registration_number_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'registration_number_many'
        
    id = fields.Integer()
    ngo_id = fields.Str(required=True)
    pan_no = fields.Str()
    pan_regdate = fields.Date()
    fcra_no = fields.Str()
    fcra_regdate = fields.Date()
    rn_12A_no = fields.Str()
    rn_12A_regdate = fields.Date()
    rn_80G_no = fields.Str()
    rn_80G_regdate = fields.Date()
    rn_35AC_no = fields.Str()
    rn_35AC_regdate = fields.Date()

    registration_office = Relationship(
        self_view = 'registration_number_registration_office',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'registration_office_one',
        related_view_kwargs = {'id': '<id>'},
        many = False,
        schema = 'RegistrationOfficeSchema',
        type_ = 'registration_office')