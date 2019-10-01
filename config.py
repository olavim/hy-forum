import os
import bcrypt
from dotenv import load_dotenv, find_dotenv

reloader_extra_files = [
	'.env',
	'application/static/scss/default.scss',
	'application/static/scss/bootstrap-overrides.scss'
]
load_dotenv(find_dotenv())
server_port = os.getenv('PORT', '5000')
env = os.getenv('FLASK_ENV', 'development')

raw_db_path = os.getenv('DATABASE_URL')
project_root = os.path.dirname(__file__)
db_path = raw_db_path.replace('%PROJECT_ROOT%', project_root)

admin_password_hash = bcrypt.hashpw(os.getenv('ADMIN_PASSWORD').encode('utf8'), bcrypt.gensalt()) \
	if os.getenv('ADMIN_PASSWORD') else None

FLASK_ENV = env
DEBUG = os.getenv('DEBUG') == 'True' if os.getenv('DEBUG') else env == 'development'
PROPAGATE_EXCEPTIONS = False
SECRET_KEY = os.getenv('SESSION_SECRET', os.urandom(32))
SQLALCHEMY_DATABASE_URI = db_path
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
DATABASE_CONNECT_OPTIONS = {}
THREADS_PER_PAGE = 8
SEND_FILE_MAX_AGE_DEFAULT = 0
CSRF_ENABLED = True
CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_SECRET', os.urandom(32))
