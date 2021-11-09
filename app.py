from flask import Flask

from config import SECRET_KEY


# Create a new Flask application
app = Flask(__name__)

# Set up SQLAlchemy
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Daanmatch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False