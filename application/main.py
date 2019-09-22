import sys
from flask import Flask
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_assets import Environment, Bundle
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Assets in static folder are cached pretty strongly, which is problematic for custom JS scripts.
# We use Flask-Assets to solve this by combining these scripts and making them available in a build-specific URI.
assets = Environment(app)
js = Bundle('js/*', filters='rjsmin', output='js/gen/bundle.js')
assets.register('js_all', js)

from .views.auth import mod as auth_module
from .views.topics import mod as topics_module
from .views.threads import mod as threads_module
from .views.messages import mod as messages_module
app.register_blueprint(auth_module)
app.register_blueprint(topics_module)
app.register_blueprint(threads_module)
app.register_blueprint(messages_module)

import application.models.user
import application.models.topic
import application.models.thread
import application.models.message
db.create_all()

def start_server():
	if config.env == 'development':
		app.run(debug=True, port=config.server_port, extra_files=config.reloader_extra_files)
	else:
		serve(app, host='0.0.0.0', port=config.server_port)
