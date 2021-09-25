from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
from marshmallow_enum import EnumField

from utils.sdg import SDG

class ActivitySchema(Schema):
    class Meta:
        type_ = 'activity'
        self_view = 'activity_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'activity_many'
        
    id = fields.Integer()
    ngo_id =  fields.Str()
    name = fields.Str()
    description = fields.Str()
    date = fields.Date()
    issue = fields.Str() 
    sdg = EnumField(SDG)
    beneficiaries = fields.Str()
    address = fields.Str()
    state = fields.Str()
    district = fields.Str()
    city = fields.Str()
    gram_panchayat = fields.Str()
    latitude = fields.Decimal()
    longitude = fields.Decimal()