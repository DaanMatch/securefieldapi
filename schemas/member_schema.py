from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema, Relationship

class MemberSchema(Schema):
    """
    Acts as the abstraction layer between the member table and user. 
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
            URL endpoint to an individual member
        self_view_kwargs:
            Fields for self_view to pass to URL
            
    password:
        Only allowed to set pw (load_only)
    field_data:

    other fields:
        Read only (dump_only)
    """

    class Meta:
        type_ = 'member'
        self_view = 'member_one'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer()
    name = fields.Str(dump_only=True)
    mobile = fields.Str(dump_only=True)
    email = fields.Str(dump_only=True)
    data_manager = fields.Str(dump_only=True)
    password = fields.Str(load_only=True)


    # args similar to meta class attributes
    field_data = Relationship(
        related_view = 'field_data_many',
        related_view_kwargs = {'id': '<id>'},
        many = True, 
        schema = 'FieldDataSchema',
        type_ = 'field_data')