
# Note: I have no idea if this works yet. 

from flask import jsonify, request
import jwt
from functools import wraps

from config import SECRET_KEY
from models import Member

# Create decorator for authorization:
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, SECRET_KEY)
            current_member = Member.query.filter_by(id=data['member_id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_member, *args, **kwargs)

    return decorator
