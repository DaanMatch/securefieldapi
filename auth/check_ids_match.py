from flask_rest_jsonapi.exceptions import AccessDenied
from flask import request
import jwt

from setup.config import SECRET_KEY

def check_member_ids_match(requested_resource_member_id):
    """
    Make sure the member_id in the token is the same as the 
    member_id of the resource that the user is trying to access.

    Params
    ------
    requested_resource_member_id:
        The member_id of the requested resource.
    """
    token = request.headers['x-access-tokens']
    token_data = jwt.decode(token, SECRET_KEY)
    if requested_resource_member_id != token_data['member_id']:
        raise AccessDenied(
            {'parameter': 'id'}, 
            "Member {} cannot access member {}'s field_data".format(
                token_data['member_id'], requested_resource_member_id
            )
        )