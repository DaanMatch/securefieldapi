from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

class DaanmatchNgoSchema(Schema):
    """
    Acts as the abstraction layer between the daanmatch_ngo table and 
    user. This class allows us to control what fields 
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
            URL endpoint to an individual daanmatch_ngo
        self_view_kwargs:
            Fields for self_view to pass to URL
        self_view_many:
            URL endpoint to all daanmatch_ngos
    """

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