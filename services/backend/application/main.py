import application.settings
import os
from waitress import serve
from application.api.routes import app

def start_server():
	port = os.getenv('PORT', '5000')

	if os.getenv('FLASK_ENV', 'development') == 'development':
		app.run(debug=True, port=port)
	else:
		serve(app, host='0.0.0.0', port=port)
