import settings
import os
from waitress import serve
from api.routes import app

def main():
	port = os.getenv('PORT', '5000')

	if os.getenv('FLASK_ENV', 'development') == 'development':
		app.run(debug=True, port=port)
	else:
		serve(app, host='0.0.0.0', port=port)

if __name__ == '__main__':
	main()
