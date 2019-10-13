from functools import wraps
from flask import abort, request
from flask_login import current_user
from .models.user import User

def require_permission(permission):
	def decorator(func):
		@wraps(func)
		def decorated_view(*args, **kwargs):
			if not current_user.has(permission):
				abort(403)
			return func(*args, **kwargs)
		return decorated_view
	return decorator

def require_permission_or_owner(permission, Model, pkey = 'id'):
	def decorator(func):
		@wraps(func)
		def decorated_view(*args, **kwargs):
			resource = Model.query.get(kwargs[pkey])
			del kwargs[pkey]

			if not resource:
				abort(404)

			if not current_user.has(permission) and resource.user.id != current_user.id:
				abort(403)

			kwargs[Model.__tablename__] = resource
			return func(*args, **kwargs)
		return decorated_view
	return decorator

def get_resource(Model, pkey = 'id'):
	def decorator(func):
		@wraps(func)
		def decorated_view(*args, **kwargs):
			resource = Model.query.get(kwargs[pkey])
			del kwargs[pkey]

			if not resource:
				abort(404)

			kwargs[Model.__tablename__] = resource
			return func(*args, **kwargs)
		return decorated_view
	return decorator

def get_non_admin_user(pkey = 'id'):
	def decorator(func):
		@wraps(func)
		def decorated_view(*args, **kwargs):
			user = User.query.get(kwargs[pkey])
			del kwargs[pkey]

			if not user:
				abort(404)
			if user.is_admin:
				abort(403)

			kwargs['user'] = user
			return func(*args, **kwargs)
		return decorated_view
	return decorator

def paginated(func):
	@wraps(func)
	def decorated_view(*args, **kwargs):
		kwargs['page'] = int(request.args.get('page') or '1')
		return func(*args, **kwargs)
	return decorated_view