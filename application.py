from setup.app import app # Import the Flask() app to prevent circular imports
from setup.db import db # SQLAlchemy object imported to prevent circular imports
from setup.api import api # Api object imported from flask_rest_jsonapi to prevent circular imports
from models import *
from schemas import *
from resource_managers import *
from routes import *


# delayed initialization
db.init_app(app)

# Create the tables
with app.app_context():
    db.create_all()

# delayed initialization
api.init_app(app)

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)