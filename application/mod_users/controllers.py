import os
import bcrypt
from flask import Blueprint, Response, request, json
from application.main import db
from .models import User

mod_users = Blueprint('users', __name__, url_prefix='/users')

def map_user(u):
	return {
		'id': u.id,
		'username': u.username,
		'created_at': u.created_at.isoformat() if u.created_at != None else u.created_at,
		'updated_at': u.updated_at.isoformat() if u.updated_at != None else u.updated_at
	}

def json_response(status, data):
	return Response(
		response=json.dumps(data),
		status=status,
		mimetype='application/json'
	)

@mod_users.route('/', methods=['GET'])
def list_users():
	users = list(map(map_user, User.query.all()))
	return json_response(200, {
		'results': users,
		'pageInfo': {'total': len(users)}
	})

@mod_users.route('/<id>', methods=['GET'])
def get_user(id):
	user = User.query.get(id)
	return json_response(200, map_user(user))

@mod_users.route('/', methods=['POST'])
def create_user():
	username = request.form.get('username')
	password = request.form.get('password')

	if len(username) < 4:
		return json_response(400, {'message': 'Username must be at least 4 characters'})

	if len(password) < 4:
		return json_response(400, {'message': 'Password must be at least 4 characters'})

	pw_hash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

	user = User(username, pw_hash)
	db.session().add(user)
	db.session().commit()

	return json_response(200, map_user(user))

@mod_users.route('/<id>', methods=['DELETE'])
def delete_user(id):
	user = User.query.get(id)
	db.session().delete(user)
	db.session().commit()
	return json_response(200, map_user(user))