from flask import render_template, url_for,redirect
from flask_login import login_required
from . import main
from flask_login import current_user
from . forms import PitchForm,CommentForm
from ..models import Pitch, Comment, User
from .. import db

@main.route('/')
def index():
    pitches=Pitch.query.all()



    return render_template('index.html',entries=pitches)


@main.route('/pitch',methods=['GET','POST'])
def pitch():
    pitch_form=PitchForm()
    if pitch_form.validate_on_submit():
        pitch=Pitch(category=pitch_form.category.data,pitch=pitch_form.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('pitch.html',pitch_form=pitch_form)
@main.route('/comment',methods=['GET','POST'])
@login_required
def comment():

    comment_form=CommentForm()
    if comment_form.validate_on_submit():
        comment=Comment(comment=comment_form.comment.data)
        db.session.add(comment)
        db.session.commit()
        # return redirect(url_for('main.index'))

    comments=Comment.query.all()
    return render_template('comment.html',comment_form=comment_form,comments=comments)
