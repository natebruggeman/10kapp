
import models

from flask import request, jsonify, Blueprint
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict


users = Blueprint('users', 'users')



@users.route('/register', methods=['POST'])
def register():
  payload = request.get_json()
  payload['email'].lower() 

  try: 
    models.User.get(models.User.email == payload['email'])
    return jsonify(data={}, status={'code': 401, "message": "A user with that email already exists"})

  except models.DoesNotExist:
    payload['password'] = generate_password_hash(payload['password'])
    user = models.User.create(**payload)
    login_user(user)
    user_dict = model_to_dict(user)
    del user_dict['password']
    return jsonify(data=user_dict, status={'code': 201, 'message': 'Successfully registered {}'.format(user_dict['email'])})






@users.route('/login', methods=['POST'])
def login():
  payload = request.get_json()

  try:

    user = models.User.get(models.User.email == payload['email'])
    user_dict = model_to_dict(user) 
    if(check_password_hash(user_dict['password'], payload['password'])):
      login_user(user) 
      del user_dict['password']
      return jsonify(data=user_dict, status={'code': 200, 'message': "Succesfully logged in {}".format(user_dict['email'])})

    else:
      print('password is wrong')
      return jsonify(data={}, status={'code': 401, 'message': 'Email or password is incorrect'})

  except models.DoesNotExist:
    print('email is incorrect')
    return jsonify(data={}, status={'code': 401, 'message': 'Email or password is incorrect'})




@users.route('/', methods=['GET'])
def list_users():
	users = models.User.select()
	for u in users: 
		user_dicts = [model_to_dict(u) for u in users]

def remove_password(u):
	u.pop('password')
	return u

	user_dicts_without_pw = list(map(remove_password, user_dicts)) 
	return jsonify(data=user_dicts_without_pw)




@users.route('/logged_in', methods=['GET'])
def get_logged_in_user(): 
	if not current_user.is_authenticated:
		return jsonify(data={}, status={
			'code': 401,
			'message': "No user is currently logged in."
		})
	else: 
		user_dict = model_to_dict(current_user)
		user_dict.pop('password')
		return jsonify(data=user_dict, status={
			'code': 200, 
			'message': "Current user is {}".format(user_dict['email'])
		})  





@users.route('/logout', methods=['GET'])
def logout():
	logout_user()

	return jsonify(data={}, status={
		'code': 200,
		'message': "Successfully logged out "
		})



