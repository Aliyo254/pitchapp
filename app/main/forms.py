from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import InputRequired,Email,EqualTo
# from wtforms import ValidationError




class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[InputRequired(),Email()])
    password = PasswordField('Password',validators =[InputRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')