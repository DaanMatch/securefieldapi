from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
from marshmallow_enum import EnumField

from utils.sdg import SDG

class ActivitySchema(Schema):
    """
    Acts as the abstraction layer between the activity table and user. 
    This class allows us to control what fields 
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
            Specifies the type.
        self_view:
            URL endpoint to an individual activity
        self_view_kwargs:
            Fields for self_view to pass to URL
        self_view_many:
            URL endpoint to all activities
    sdg:
        SDG class currently not implemented. Likeley to be removed.
    """

    class Meta:
        type_ = 'activity'
        self_view = 'activity_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'activity_many'
        
    id = fields.Integer() # An id field is required in the schema
    ngo_id =  fields.Str(required=True)
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