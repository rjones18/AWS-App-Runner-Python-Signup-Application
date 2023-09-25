from flask import Flask

application = Flask(__name__, static_url_path='/app/static') # Path to the Bootstrap CSS code
application.config['SECRET_KEY'] = 'XXXX' # Each Flask web application contains a secret key which used to sign session cookies for protection against cookie data tampering.
from app import routes  # Avoid circular imports. Example of this would be naming your file the same as a python module.
