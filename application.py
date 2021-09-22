from flask import Flask
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
from flask_sqlalchemy import SQLAlchemy
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Relationship, Schema

# Create a new Flask application
app = Flask(__name__)


# Set up SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ngos.db'
db = SQLAlchemy(app)


# Create data storage
class RegistrationOffice(db.Model):
    id =  db.Column(db.CHAR, primary_key=True)
    registered_with = db.Column(db.String)
    date = db.Column(db.Date)
    address = db.Column(db.String)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)

class RegistrationNumber(db.Model):
    id =  db.Column(db.CHAR, 
        db.ForeignKey('registration_office.id'), 
        primary_key=True)
    pan_no = db.Column(db.CHAR)
    pan_regdate = db.Column(db.Date)
    fcra_no = db.Column(db.CHAR)
    fcra_regdate = db.Column(db.Date)
    rn_12A_no = db.Column(db.CHAR)
    rn_12A_regdate = db.Column(db.Date)
    rn_80G_no = db.Column(db.CHAR)
    rn_80G_regdate = db.Column(db.Date)
    rn_35AC_no = db.Column(db.CHAR)
    rn_35AC_regdate = db.Column(db.Date)

    registration_office = db.relationship('RegistrationOffice', 
        backref=db.backref('registration_numbers'))

# Create the tables
db.create_all()



# Create data abstraction 
class RegistrationOfficeSchema(Schema):
    class Meta:
        type_ = 'registration_office'
        self_view = 'registration_office_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'registration_office_many'

    id =  fields.Str()
    registered_with = fields.Str()
    date = fields.Date()
    address = fields.Str()
    latitude = fields.Decimal()
    longitude = fields.Decimal()

    registration_numbers = Relationship(self_view = 'registration_office_registration_numbers',
        self_view_kwargs = {'id': '<id>'},
        related_view = 'registration_number_many',
        many = True,
        schema = 'RegistrationNumberSchema',
        type_ = 'registration_number')

class RegistrationNumberSchema(Schema):
    class Meta:
        type_ = 'registration_number'
        self_view = 'registration_number_one'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'registration_number_many'
        
    id =  fields.Str()
    pan_no = fields.Str()
    pan_regdate = fields.Date()
    fcra_no = fields.Str()
    fcra_regdate = fields.Date()
    rn_12A_no = fields.Str()
    rn_12A_regdate = fields.Date()
    rn_80G_no = fields.Str()
    rn_80G_regdate = fields.Date()
    rn_35AC_no = fields.Str()
    rn_35AC_regdate = fields.Date()


# Create resource managers
class RegistrationOfficeMany(ResourceList):
    schema = RegistrationOfficeSchema
    data_layer = {'session': db.session,
                  'model': RegistrationOffice}

class RegistrationOfficeOne(ResourceDetail):
    schema = RegistrationOfficeSchema
    data_layer = {'session': db.session,
                  'model': RegistrationOffice}

class RegistrationNumberMany(ResourceList):
    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}

class RegistrationNumberOne(ResourceDetail):
    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}

class RegistrationOfficeRegistrationNumber(ResourceDetail):
    schema = RegistrationNumberSchema
    data_layer = {'session': db.session,
                  'model': RegistrationNumber}

# Create endpoints
api = Api(app)
api.route(RegistrationOfficeMany, 'registration_office_many', '/registration_offices')
api.route(RegistrationOfficeOne, 'registration_office_one', '/registration_office/<string:id>')
api.route(RegistrationNumberMany, 'registration_number_many', '/registration_numbers')
api.route(RegistrationNumberOne, 'registration_number_one', '/registration_number/<string:id>')
api.route(RegistrationOfficeRegistrationNumber, 
    'registration_office_registration_numbers', 
    '/registration_office/<string:id>/relationships/registration_numbers')



# main loop to run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)