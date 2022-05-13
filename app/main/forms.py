from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,SelectField
from wtforms.validators import DataRequired



class PitchForm(FlaskForm):
    category=SelectField('category',
        choices=[('inspiration', 'inspiration'), ('life hacks', 'life hacks'), ('tech', 'tech'), ('funny', 'funny')], validators = [DataRequired()])
    pitch = TextAreaField('pitch',validators=[DataRequired()])
    submit = SubmitField('submit')

class CommentForm(FlaskForm):
    comment=TextAreaField('comment',validators=[DataRequired()])
    submit = SubmitField('submit')
