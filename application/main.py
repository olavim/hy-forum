from flask import Flask
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
import application.config as config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from .mod_users.controllers import mod_users as user_module
app.register_blueprint(user_module)

def start_server():
	if config.env == 'development':
		app.run(debug=True, port=config.server_port)
	else:
		serve(app, host='0.0.0.0', port=config.server_port)
