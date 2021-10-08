from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema

class MemberSchema(Schema):
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
            
    sdg:
        Currently implemented as char in db. Might switch to type
        enum.
    """

    class Meta:
        type_ = 'member'
        self_view = 'member_one'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer()
    name = fields.Str()
    mobile = fields.Str()
    email = fields.Str()
    mobile_device_id = fields.Str()
    password = fields.Str(load_only=True)