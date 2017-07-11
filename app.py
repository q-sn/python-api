import os
import json
from models.user import User
from flask import Flask
from flask import jsonify
from flask import request
from flask import session

app = Flask(__name__)


@app.route('/user/register/', methods=['POST'])
def addUser():
	login = request.args.get('login')
	password = request.args.get('password')

	if User.check(login):
		return jsonify({
			'errors': 'user exist'
		})
	else:
		if User.add(login, password):
			return json.dumps([login, password])


@app.route('/users/view/', methods=['GET'])
def getUsers():
	users = User.getUsers()

	return json.dumps(users)


@app.route('/user/delete/', methods=['DELETE'])
def delete():
	login = request.args.get('login')

	if User.check(login):
		User.delete(login)
		return jsonify({
			'success': 'user deleted'
		})
	else:
		return jsonify({
			'errors': 'user does not exist'
		})


@app.route('/user/login/', methods=['POST'])
def login():
	login = request.args.get('login')
	password = request.args.get('password')

	if User.checkPassword(login, password):
		session['login'] = login
		return jsonify({
			'success': 'session created'
		})
	else:
		return jsonify({
			'errors': 'wrong password'
		})


@app.route('/user/logout/', methods=['POST'])
def logout():
	if 'login' in session:
		session.pop('login', None)
		return jsonify({
			'success': 'session deleted'
		})
	return jsonify({
		'errors': 'session does not exist'
	})


@app.route('/user/isauth/', methods=['POST'])
def isAuth():
	if 'login' in session:
		return jsonify({
			'state': 'authorized'
		})
	return jsonify({
		'state': 'not authorized'
	})


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
