# -*- coding: utf-8 -*-
from flask import Flask, make_response, render_template

# Importing User Api library
from google.appengine.api import users

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():

    # Get Google User
    user = users.get_current_user()

    # we haven't to validate if we are logged. Because we force the auth by yaml.
    response = make_response(render_template('index.html', USER=user.nickname()))
    response.headers['Content-Type'] = 'text/html'
    return response
