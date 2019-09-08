import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

database_url = os.getenv('DATABASE_URL')
server_port = os.getenv('PORT', '5000')
env = os.getenv('FLASK_ENV', 'development')