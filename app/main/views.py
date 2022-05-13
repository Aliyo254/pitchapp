from flask import render_template, url_for
from . import main
from . forms import PitchForm

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/pitch',methods=['GET','POST'])
def pitch():
    pitch_form=PitchForm()
    return render_template('pitch.html',pitch_form=pitch_form)