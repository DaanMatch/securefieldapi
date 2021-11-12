import re

from models import People

def get_roles(member_id):
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