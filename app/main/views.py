from flask import render_template, url_for,redirect
from . import main
from . forms import PitchForm
from ..models import Pitch
from .. import db

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/pitch',methods=['GET','POST'])
def pitch():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        pitch=Pitch(category=pitch_form.category.data,pitch=pitch_form.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('pitch.html',pitch_form=pitch_form)