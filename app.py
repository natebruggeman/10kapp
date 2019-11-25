from flask import Flask, jsonify, g 
from flask_cors import CORS
from flask_login import LoginManager
from resources.skills import skill_bp
from resources.users import users

import models


DEBUG = True
PORT = 8000


app = Flask(__name__)

app.secret_key = "Secret Key Nate rules, Conrad drools"
login_manager = LoginManager()
login_manager.init_app(app)



@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None	
		

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(data={
		'error': 'User not logged in.'
		}, status={
		'code': 401,
		'message': "You must be logged in to access that resource."
	}), 401


CORS(skill_bp, origins=['http://localhost:3000'], supports_credentials=True) 
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(skill_bp, url_prefix='/api/v1/skills')
app.register_blueprint(users, url_prefix='/api/v1/users')


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response




# @app.route('/')
# def index():
#     return 'Hello Nate(sexy) and Conrad'




if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)







