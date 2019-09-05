import settings
import os
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def root():
	return 'Hello World!'

port = os.getenv('PORT', '5000')

def main():
	if os.getenv('FLASK_ENV', 'development') == 'development':
		app.run(debug=True, port=port)
	else:
		serve(app, host='0.0.0.0', port=port)

if __name__ == '__main__':
	main()