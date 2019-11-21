from flask import Flask, jsonify, g 
from flask_cors import CORS
from flask_login import LoginManager
from resources.skills import skill


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


@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    return 'hello Nate and Conrad'




if __name__ == '__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)





