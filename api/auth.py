from app import api
from flask import make_response, jsonify, request
from flask_restplus import abort, Resource
from utils.request_handling import *

auth = api.namespace('auth', description="Authentication Services")

@auth.route("/login", strict_slashes=False)
class Login(Resource):

    @auth.response(200, 'Success')
    @auth.response(400, 'Missing args')
    @auth.response(403, 'Not register')
    @auth.param('password', 'Password of user')
    @auth.param('username', 'Username of user')
    @auth.doc(description="Please enter username and password. "
                          "If the username and password correct, a token will be returned")
    def post(self):
        username = get_request_args("username", str)
        password = get_request_args("password", str)


        return make_response(jsonify(username=username,password=password), 200)
