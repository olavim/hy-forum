import os
from dotenv import load_dotenv, find_dotenv

reloader_extra_files = ['application/static/scss/default.scss']

load_dotenv(find_dotenv())
server_port = os.getenv('PORT', '5000')
env = os.getenv('FLASK_ENV', 'development')
database_schema = os.getenv('DATABASE_SCHEMA') or None

DEBUG = False

SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = DEBUG
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"
