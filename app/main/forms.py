from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,SelectField
from wtforms.validators import InputRequired



class PitchForm(FlaskForm):
    category=SelectField('category',
        choices=[('inspiration', 'inspiration'), ('life hacks', 'life hacks'), ('tech', 'tech'), ('funny', 'funny')], validators = [InputRequired()])
    pitch = TextAreaField('pitch',validators=[InputRequired()])
    submit = SubmitField('submit')