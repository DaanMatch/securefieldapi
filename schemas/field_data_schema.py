from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
from marshmallow_enum import EnumField

from utils.sdg import SDG

class FieldDataSchema(Schema):
    """
    Acts as the abstraction layer between the field_data table and user. 
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
            URL endpoint to an individual NGO's field_data
        self_view_kwargs:
            Fields for self_view to pass to URL
        self_view_many:
            URL endpoint to all field_data for all NGOs
            
    sdg:
        SDG class currently not implemented. Likeley to be removed.
    """

    class Meta:
        type_ = 'field_data'
        self_view = 'field_data_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'field_data_many'
        
    id = fields.Str(required=True)
    ngo_id =  fields.Str(required=True)
    recorded_by = fields.Str()
    description = fields.Str()
    date = fields.Date()
    sector_id = fields.Str()
    sdg = EnumField(SDG)
    beneficiaries = fields.Str()
    address = fields.Str()
    state_id = fields.Str()
    district_id = fields.Str()
    latitude = fields.Decimal()
    longitude = fields.Decimal()
    title = fields.Str()
    comment = fields.Str()
    media = fields.Str()
