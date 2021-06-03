import os
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder

# init Flask
app = Flask(__name__)

# Basic config with security for forms and session cookie
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'thisismyscretkey'

# Init SQLAlchemy
db = SQLA(app)
db.create_all()
# Init F.A.B.
appbuilder = AppBuilder(app, db.session)

# Run the development server
app.run(host='0.0.0.0', port=8080, debug=True)