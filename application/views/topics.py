import os
import bcrypt
from flask import Blueprint, request, json, session, redirect, url_for, g, render_template, flash
from ..main import db
from ..models.user import User
from ..forms.auth import RegisterForm, LoginForm

mod = Blueprint('topics', __name__, url_prefix='/')

@mod.before_request
def before_request():
	g.user = None
	if 'user_id' in session:
		g.user = User.query.get(session['user_id'])

@mod.route('/', methods=['GET'])
def home():
	return render_template("topics/home.j2", user=g.user)
