import application.settings
import os
import re
from flask_cors import CORS
from waitress import serve
from .api.routes import app
from .database.setup import db

def start_server():
	app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URL')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config["SQLALCHEMY_ECHO"] = True
	db.init_app(app)

	cors_origins_pattern = re.compile(os.getenv('CROSS_ORIGINS', '.*'))
	CORS(app, resources={r'*': {'origins': cors_origins_pattern}})

	port = os.getenv('PORT', '5000')

	if os.getenv('FLASK_ENV', 'development') == 'development':
		app.run(debug=True, port=port)
	else:
		serve(app, host='0.0.0.0', port=port)
