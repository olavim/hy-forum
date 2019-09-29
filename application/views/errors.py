from flask import render_template
from ..main import app

@app.errorhandler(403)
def forbidden(_):
	return render_template('errors/403.html'), 403

@app.errorhandler(404)
def page_not_found(_):
	return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(_):
	return render_template('errors/500.html'), 500
