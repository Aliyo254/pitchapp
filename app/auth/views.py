from flask import render_template, url_for
from . import auth
from .forms import LoginForm

@auth.route('/login')
def login():
    login_form = LoginForm()

    return render_template('auth/login.html', login_form=login_form)