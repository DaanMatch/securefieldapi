from setup.app import app # Import the Flask() app to prevent circular imports
from setup.db import db # SQLAlchemy object imported to prevent circular imports
from setup.api import api # Api object imported from flask_rest_jsonapi to prevent circular imports
from models import *
from schemas import *
from resource_managers import *
from routes import *
from limiter import limiter


db.init_app(app) # delayed initialization

# Create the tables
with app.app_context():
    db.create_all()

api.init_app(app) # delayed initialization

# login route, move me later
from auth.login import login_member
@limiter.limit("6/10minutes")
@app.route('/login', methods=['GET', 'POST']) 
def login():
    return login_member()

# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)