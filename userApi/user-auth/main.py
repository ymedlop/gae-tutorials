# -*- coding: utf-8 -*-
from flask import Flask, make_response, render_template

# Importing User Api library
from google.appengine.api import users

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():

    # Get Google User
    user = users.get_current_user()

    if user:
        greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' % (user.nickname(), users.create_logout_url('/')))
    else:
        greeting = ('<a href="%s">Sign in or register</a>.' % users.create_login_url('/'))

    response = make_response(render_template('index.html', GREETING=greeting))
    response.headers['Content-Type'] = 'text/html'
    return response
