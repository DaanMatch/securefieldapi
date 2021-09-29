"""
General format for each schema:
...

# All schema data abstractions inherit from marshmallow_jsonapi.Schema
# id and Meta.type_ are required

class TableNameSchema(Schema):

    # Class specifies metadata to be sent back to the user.
    class Meta:
        type_ = 'table_name'
        self_view = 'table_name_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'table_name_many'
        
    # Specify fields to accept from/sent back to the user.
    id = fields.Integer()
    ngo_id = fields.Str(required=True)
    attr_1 = fields...

    # These args function similarly to those in the Meta class
    child/children = Relationship(
        self_view = 'table_name_child/children',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'child/children_one',
        related_view_kwargs = {'id': '<id>'},
        many = True/False,
        schema = 'Child/ChildrenSchema',
        type_ = child/children)
"""

from .activity_schema import *
from .daanmatch_ngo_schema import *
from .operation_schema import *
from .registration_number_schema import *
from .registration_office_schema import *
