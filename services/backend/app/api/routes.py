import os
import re
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors_origins_pattern = re.compile(os.getenv('CROSS_ORIGINS', '.*'))
CORS(app, resources={r'*': {'origins': cors_origins_pattern}})

@app.route('/')
def root():
	return 'Hello World'
