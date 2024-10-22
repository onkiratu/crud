from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from Grade_12.models import User  


class SignUpForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()]) 
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm password", validators=[DataRequired(),  EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()]) 
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

class ResultForm(FlaskForm):
    id = IntegerField("ID", validators=[DataRequired()])
    math = IntegerField("Math", validators=[DataRequired()])
    english = IntegerField("English", validators=[DataRequired()])
    applied_computing = IntegerField("Applied computing", validators=[DataRequired()])
    algorithmics = IntegerField("Algorithmics", validators=[DataRequired()])
    submit = SubmitField("Submit")



    