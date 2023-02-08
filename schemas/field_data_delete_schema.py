from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

class FieldDataDeleteSchema(Schema):
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
        Currently implemented as char in db. Might switch to type
        enum.
    """

    class Meta:
        type_ = 'field_data'
        self_view = 'field_data_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'field_data_many'

    id = fields.Integer()
    ngo_id = fields.Integer(required=True)
    recorded_by = fields.Integer(dump_only=True)
    date = fields.Date(dump_only=True)
    address = fields.Str(dump_only=True)
    latitude = fields.Decimal(dump_only=True)
    longitude = fields.Decimal(dump_only=True)
    title = fields.Str(dump_only=True)
    comment = fields.Str(dump_only=True)
    media = fields.Str(dump_only=True)
    media_type = fields.Str(dump_only=True)
    sector_id = fields.Integer(dump_only=True)
    sdg = fields.Str(dump_only=True)
    deleted = fields.Boolean()
