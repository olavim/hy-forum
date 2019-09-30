from functools import wraps
from flask import abort
from flask_login import current_user

def require_permission(permission):
	def decorator(func):
		@wraps(func)
		def decorated_view(*args, **kwargs):
			if not current_user.has(permission):
				abort(403)
			return func(*args, **kwargs)
		return decorated_view
	return decorator