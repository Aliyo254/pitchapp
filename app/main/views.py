from flask import render_template
from . import main
from .forms import LoginForm

@main.route('/')
def index():
    login_form = LoginForm()

    return render_template('index.html', login_form=login_form)