from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema
from marshmallow_enum import EnumField

from utils.sdg import SDG

class OperationSchema(Schema):
    class Meta:
        type_ = 'operation'
        self_view = 'operation_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'operation_many'

    id = fields.Integer()
    ngo_id = fields.Str()
    issues = fields.Str()
    sdgs = EnumField(SDG)
    states = fields.Str()
    cities = fields.Str()
    district = fields.Str()
    gram_panchayats = fields.Str()

    activities = Relationship(
        self_view = 'operation_activities',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'activity_many',
        many = False,
        schema = 'ActivitySchema',
        type_ = 'activity'
    )