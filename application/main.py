import sys
from flask import Flask
from waitress import serve
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_assets import Environment, Bundle
from flask_login import LoginManager
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# Manager handles CLI stuff for Flask-Migrate
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Assets in static folder are cached pretty strongly, which is problematic for custom JS scripts.
# We use Flask-Assets to solve this by combining these scripts and making them available in a build-specific URI.
assets = Environment(app)
js = Bundle('js/*', filters='rjsmin', output='js/gen/bundle.js')
assets.register('js_all', js)

# Register views
import application.views.context
import application.views.errors
from .views.auth import mod as auth_module
from .views.search import mod as search_module
from .views.admin import mod as admin_module
from .views.topics import mod as topics_module
from .views.threads import mod as threads_module
from .views.messages import mod as messages_module

app.register_blueprint(auth_module)
app.register_blueprint(search_module)
app.register_blueprint(admin_module)
app.register_blueprint(topics_module)
app.register_blueprint(threads_module)
app.register_blueprint(messages_module)

# Import models so that alembic can find them
import application.models.user
import application.models.role
import application.models.topic
import application.models.thread
import application.models.message

# Turn foreign key support on in sqlite3. Needed for foreign key constraints.
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

@event.listens_for(Engine, 'connect')
def _set_sqlite_pragma(dbapi_connection, connection_record):
	if isinstance(dbapi_connection, SQLite3Connection):
		cursor = dbapi_connection.cursor()
		cursor.execute('PRAGMA foreign_keys=ON;')
		cursor.close()
