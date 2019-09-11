from flask import Flask
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
import application.config as config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from .views.auth import mod as auth_module
from .views.topics import mod as topics_module
from .views.threads import mod as threads_module
from .views.messages import mod as messages_module
app.register_blueprint(auth_module)
app.register_blueprint(topics_module)
app.register_blueprint(threads_module)
app.register_blueprint(messages_module)

def start_server():
	if config.env == 'development':
		app.run(debug=True, port=config.server_port, extra_files=config.reloader_extra_files)
	else:
		serve(app, host='0.0.0.0', port=config.server_port)
