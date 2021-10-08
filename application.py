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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ngos.db'
db.init_app(app) # delayed initialization


# Create the tables
with app.app_context():
    db.create_all()


api.init_app(app) # delayed initialization


# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)