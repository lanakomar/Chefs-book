from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
import re

from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')


def is_strong_password(form, field):
    password = field.data
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pattern = re.compile(reg)

    # searching regex
    match = re.search(pattern, password)

    # validating conditions
    if not match:
        raise ValidationError("Password should have at least one number, one special symbol, one uppercase and one lowercase character. Password shold be 6 - 20 characters long.")


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired("This field is required."), username_exists,\
            Length(max=40, message="First name should be less than 40 characters.")])
    email = StringField('email', validators=[DataRequired(message="This field is required."), user_exists,\
        Email(message="Please, provide a valid email address.")])
    password = StringField('password', validators=[DataRequired(message="This field is required."), is_strong_password])
