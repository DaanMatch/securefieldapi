from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

class DaanmatchNgoSchema(Schema):
    class Meta:
        type_ = 'daanmatch_ngo'
        self_view = 'daanmatch_ngo_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'daanmatch_ngo_many'

    id = fields.Integer()
    ngo_id = fields.Str(required=True)
    name = fields.Str()
    description = fields.Str()
    majoracivity_description = fields.Str()
    type = fields.Str()
    last_updated = fields.DateTime()
    address = fields.Str()
    mobile = fields.Str()
    email = fields.Str()
    fax = fields.Str()
    website = fields.Str()
    facebook = fields.Str()
    twitter = fields.Str()
    fulltime_staff = fields.Integer()
    parttime_staff = fields.Integer()
    volunteers = fields.Integer()
    partner_ids = fields.Str()

    registration_number = Relationship(
        self_view = 'daanmatch_ngo_registration_number',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'registration_number_one',
        related_view_kwargs={'id': '<id>'},
        many = False,
        schema = 'RegistrationNumberSchema',
        type_ = 'registration_number')

    operation = Relationship(
        self_view = 'daanmatch_ngo_operation',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'operation_one',
        related_view_kwargs={'id': '<id>'},
        many = False,
        schema = 'OperationSchema',
        type_ = 'operation')