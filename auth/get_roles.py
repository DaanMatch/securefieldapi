from flask import request
import jwt
import re

from models import People
from setup.config import SECRET_KEY

def get_roles():
    """
    Gets the roles associated with a member id for all NGOs 
    member_id is associated with in the people table.

    Returns ngo_roles_dict in the following format:
    {
        ngo_id_1: ['OM', 'DM', ...],
        ngo_id_2: ['OM', 'DM', ...],
        ...
    }
    """
    # get the member_id from the token
    token = request.headers['x-access-tokens']
    token_data = jwt.decode(token, SECRET_KEY)
    member_id = token_data['member_id']

    ngo_roles_dict = {}

    # All people associated w/ member_id. This is really the same
    # person associated with multiple NGOs
    people = People.query.filter_by(member_id=member_id)

    for person in people:
        ngo_id = person.ngo_id

        # '{ Roles: "OM", "DM"}' => '"OM", "DM"'
        roles_string = re.search(r'Roles: (.*)}', person.designation).group(1)
        
        # '"OM", "DM"' => 'OM, DM'
        roles_string = roles_string.replace('"', '')

        # 'OM, DM' => ['OM', 'DM']
        roles_list = roles_string.split(', ')

        ngo_roles_dict[ngo_id] = roles_list

    return ngo_roles_dict