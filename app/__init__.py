"""
init flask app and api
"""

from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from flask_restplus import Api


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'hard to guess what is the key'
app.config['MAIL_SERVER'] = 'smtp.gamil.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
# TODO Change the email address
app.config['MAIL_USERNAME'] = 'xxx@gmail.com'
# TODO Change the email password
app.config['MAIL_PASSWORD'] = 'xxxx'
# TODO Change the email address
app.config['MAIL_DEFAULT_SENDER'] = 'xxx@gmail.com'

CORS(app)
api = Api(app)
mail = Mail(app)