# Import flask and SQLAlchemy
from flask import Flask, json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import HTTPException
from flask_security import Security, SQLAlchemySessionUserDatastore

from flask_principal import Principal, Permission, RoleNeed
student_permission      = Permission(RoleNeed('Student'))
staff_permission        = Permission(RoleNeed('Staff'))
supervisor_permission   = Permission(RoleNeed('Supervisor'))

# Define the WSGI application object
app = Flask(__name__)
CORS(app)

# Load Configurations and configure app
app.config.from_object('config')

# Create the DB and other objects for the app
db = SQLAlchemy(app)
mm = Marshmallow(app)

# Configure Flask Security
from api.user.models import User, Role, RolesUsers
user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, user_datastore)

#  Handle Flask Exceptions with JSON output instead of HTML
@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

# Mount the User Blueprint
from api.user.controllers import user_module
app.register_blueprint(user_module)

from api.ticket.controllers import ticket_module
app.register_blueprint(ticket_module)

from api.vote.controllers import vote_module
app.register_blueprint(vote_module)


# Create the database and tables:
app.app_context().push()
db.create_all()