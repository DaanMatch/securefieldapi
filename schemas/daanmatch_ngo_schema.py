from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

class DaanmatchNgoSchema(Schema):
    class Meta:
        type_ = 'daanmatch_ngo'
        self_view = 'daanmatch_ngo_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'daanmatch_ngo_many'

    id = fields.Integer()
    ngo_id = fields.Str()
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