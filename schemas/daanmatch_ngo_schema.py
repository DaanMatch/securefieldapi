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

    registration_number:
        Establishes a one-to-one relationship between daanmatch_ngo and 
        registration_number because registration_number.ngo_id is 
        unique (Normally many=False specifies many-to-one)
    operation:
        Establishes a one-to-one relationship between daanmatch_ngo and 
        operation because operation.ngo_id is unique (Normally 
        many=False specifies many-to-one)
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

    # These args function similarly to those in the Meta class
    registration_number = Relationship(
        self_view = 'daanmatch_ngo_registration_number',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'registration_number_one',
        related_view_kwargs={'id': '<id>'},
        many = False,
        schema = 'RegistrationNumberSchema',
        type_ = 'registration_number')

    operation = Relationship(
        self_view = 'daanmatch_ngo_operation',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'operation_one',
        related_view_kwargs={'id': '<id>'},
        many = False,
        schema = 'OperationSchema',
        type_ = 'operation')