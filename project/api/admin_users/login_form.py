import os
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    success_url = os.environ.get("ADMIN_NAMESPACE")
    login_url = os.environ.get("ADMIN_NAMESPACE") + "/login/"
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
