from flask import Flask

from db import db # SQLAlchemy object imported to prevent circular imports
from api import api # Api object imported from flask_rest_jsonapi to prevent circular imports
from models import *
from schemas import *
from resource_managers import *
from routes import *


# Create a new Flask application
app = Flask(__name__)


# Set up SQLAlchemy
app.config['SECRET_KEY'] = 'REPLACE_ME_LATER'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Daanmatch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) # delayed initialization


# Create the tables
with app.app_context():
    db.create_all()

###############################################################################
# TODO: Move this to its own file once everything tested
# Note: I have no idea if this works yet. 

from flask import jsonify, request
import jwt
from functools import wraps

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
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = Member.query.filter_by(id=data['id']).first()
        except:
            return jsonify({'message': 'token is invalid'})

        return f(current_user, *args, **kwargs)
    return decorator
###############################################################################


api.init_app(app) # delayed initialization


# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)