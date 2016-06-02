# Import flask and template operators
from flask import Flask, render_template, g
# Define the WSGI application object
app = Flask(__name__, static_folder='resources', template_folder='views')

# Import SQL
# from flask.ext.sqlalchemy import SQLAlchemy
# Define the database object which is imported by modules and controllers
# db = SQLAlchemy(app)

# Configurations
app.config.from_object('config')


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import modules
from sms.controllers.auth import auth
modules = [
    auth,
]
# Add modules to app
for module in modules:
    app.register_blueprint(auth)


# Database
from sms.repository.handler import get_db


@app.before_request
def before_request():
    get_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
