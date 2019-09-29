import os
import sys
import sass
import config
import traceback
import logging
import click
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

def start_server():
	log_section('Start HTTP server')
	print('Starting server on port {0}'.format(config.server_port))

	if config.env == 'development':
		app.run(port=config.server_port, extra_files=config.reloader_extra_files, debug=config.DEBUG)
	else:
		from waitress import serve
		serve(app, host='0.0.0.0', port=config.server_port)

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
			# We try to automatically resolve this by telling alembic (the migration tool Flask-Migrate is based on)
			# that this database equates to the first revision, and then try the migration again.
			print('Retrying migration after stamping database with baseline revision')
			stamp(revision='baseline')
			upgrade_db(False)
		else:
			logging.error(traceback.format_exc())
			raise

def ensure_admin_user():
	log_section('Ensure admin user')

	from application.models.user import User
	from application.models.role import Role, Permission

	admin_user = User.query.filter_by(username='admin').first()
	admin_role = Role.query.filter_by(name='admin').first()

	if admin_user:
		print('Admin user exists')
	else:
		print('Creating admin user...')

		if not config.admin_password:
			print('Cannot continue: Admin password not configured')
			return

		import bcrypt
		password_hash = bcrypt.hashpw(config.admin_password.encode('utf8'), bcrypt.gensalt())
		admin_user = User('admin', password_hash.decode('utf8'))

		db.session().add(admin_user)
		db.session().commit()

	if admin_role:
		print('Admin role exists')
	else:
		print('Creating admin role...')

		manage_roles_permission = Permission.query.filter_by(permission='roles:manage').first()

		admin_role = Role('admin')
		admin_role.permissions.append(manage_roles_permission)

		db.session().add(admin_role)
		db.session().commit()

	admin_user_has_role = any(role.id == admin_role.id for role in admin_user.roles)

	if admin_user_has_role:
		print('Admin user has admin role')
	else:
		print('Giving admin role to admin user...')
		admin_user.roles.append(admin_role)
		db.session().commit()

def migrate_db(first_attempt=True):
	log_section('Run database migrations')
	with app.app_context():
		upgrade_db()

def build_styles():
	log_section('Build styles')
	compile_sass_to_css(sass_map)

def main(no_migrations=False, no_assets=False, no_run=False):
	if is_running_from_reloader():
		log_section('Reloading application...', True, False)

	if not no_migrations and not is_running_from_reloader():
		migrate_db()

	if not no_assets:
		build_styles()

	if not no_run:
		ensure_admin_user()
		start_server()

@click.group(invoke_without_command=True)
@click.option('--no-migrations', is_flag=True, help='Don\'t run database migrations')
@click.option('--no-assets', is_flag=True, help='Don\'t build static assets')
@click.option('--no-run', is_flag=True, help='Don\'t run HTTP server')
@click.pass_context
def cli(ctx, no_migrations=False, no_assets=False, no_run=False):
	if ctx.invoked_subcommand is None:
		main(no_migrations, no_assets, no_run)

ctx_ignore = dict(ignore_unknown_options=True, allow_extra_args=True)

@cli.command('db', context_settings=ctx_ignore, help='Flask-Migrate CLI')
@click.option('--help', is_flag=True)
def flask_migrate(help):
	manager.run()

if __name__ == '__main__':
	cli() # pylint: disable=no-value-for-parameter
