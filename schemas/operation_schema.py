from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema
from marshmallow_enum import EnumField

from utils.sdg import SDG

class OperationSchema(Schema):
    """
    Acts as the abstraction layer between the operation table and 
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
            URL endpoint to an individual operation
        self_view_kwargs:
            Fields for self_view to pass to URL
        self_view_many:
            URL endpoint to all operation

    activities:
        Establishes a many-to-one relationship between activity and 
        operation because activity.ngo_id is not unique.
    """

    class Meta:
        type_ = 'operation'
        self_view = 'operation_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'operation_many'

    id = fields.Integer()
    ngo_id = fields.Str(required=True)
    issues = fields.Str()
    sdgs = EnumField(SDG)
    states = fields.Str()
    cities = fields.Str()
    district = fields.Str()
    gram_panchayats = fields.Str()

    # These args function similarly to those in the Meta class
    activities = Relationship(
        self_view = 'operation_activities',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'activity_many',
        many = False,
        schema = 'ActivitySchema',
        type_ = 'activity'
    )