import os
import sys
import sass
import config
import traceback
import logging
from werkzeug.serving import is_running_from_reloader
from application.main import app, db, manager
from flask_migrate import upgrade, stamp, current

sass_map = {'application/static/scss/default.scss': 'application/static/css/default.css'}

def log_section(msg, always_beefy=False, trailing_newline=True):
	if is_running_from_reloader() and not always_beefy:
		# No beefy logs with every reload
		print('\n{0}:'.format(msg))
	else:
		hline = '=' * (len(msg) + 2)
		print('\n{0}\n {1}\n{0}'.format(hline, msg))
		if trailing_newline:
			print('')

def compile_sass_to_css(sass_map):
	for source, dest in sass_map.items():
		if not os.path.exists(os.path.dirname(dest)):
			os.makedirs(os.path.dirname(dest))

		with open(dest, 'w') as outfile:
			outfile.write(sass.compile(filename=source, output_style='compressed'))

		print('%s compiled to %s' % (source, dest))

def build_styles():
	log_section('Build styles')
	compile_sass_to_css(sass_map)

def upgrade_db(first_attempt=True):
	try:
		upgrade()
	except Exception:
		print('Error: Could not run migrations')

		if first_attempt and current() == None:
			# The migrations failed and the database has no record of past migrations.
			#
			# This is likely due to the developer having a version of the database from before Flask-Migrate
			# was introduced to the project.
			#
			# Try to automatically resolve this by telling alembic (the migration tool Flask-Migrate is based on)
			# that this database equates to the first revision, and then try the migration again.
			print('Retrying migration after stamping database with baseline revision')
			stamp(revision='baseline')
			upgrade_db(False)
		else:
			logging.error(traceback.format_exc())
			raise

def migrate_db(first_attempt=True):
	log_section('Run database migrations')
	with app.app_context():
		upgrade_db()

def start_server():
	log_section('Start HTTP server')
	print('Starting server on port {0}'.format(config.server_port))

	if config.env == 'development':
		app.run(debug=True, port=config.server_port, extra_files=config.reloader_extra_files)
	else:
		from waitress import serve
		serve(app, host='0.0.0.0', port=config.server_port)

if __name__ == '__main__':
	# Run Flask-Migrate CLI if the first command line argument is 'db'
	if len(sys.argv) > 1 and sys.argv[1] == 'db':
		manager.run()
	else:
		if is_running_from_reloader():
			log_section('Reloading server...', True, False)

		if not is_running_from_reloader():
			migrate_db()

		build_styles()
		start_server()
