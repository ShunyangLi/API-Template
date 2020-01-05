"""
init flask app and api
"""

from flask import Flask
from flask_restplus import Api
from flask_cors import CORS


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SECRET_KEY'] = 'hard to guess what is the key'

api = Api(app)
CORS(app)