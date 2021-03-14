# Imports related to forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

# Imports related to users
from flask_login import current_user
from PyAny_MainApp.models import User

# Login form
class LoginForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(),Email()])
  password = PasswordField('Password',
                           validators=[DataRequired()])
  submit = SubmitField('Login')

# Registration form
class RegistrationForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(),
                                  Email()]
                      )
  username = StringField('UserName',
                         validators=[DataRequired()]
                         )
  password = PasswordField('Password',
                           validators=[DataRequired(),
                                       EqualTo('pass_confirm',
                                               message='Passwords must match!')
                                       ]
                           )
  pass_confirm = PasswordField('Confirm Password',
                               validators=[DataRequired()]
                               )
  submit = SubmitField('Register')

  def check_email(self,field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError("That email is already registered!")

  def check_username(self,field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError("That username is already registered!")

class UpdateUserForm(FlaskForm):
  email = StringField('Email',
                      validators=[DataRequired(),
                                  Email()]
                      )
  username = StringField('UserName',
                         validators=[DataRequired()]
                         )
  picture = FileField('Update Profile Picture',
                      validators=[FileAllowed(['jpg','png'])]
                      )
  submit = SubmitField('Update User')

  def check_email(self,field):
    if User.query.filter_by(email=field.data).first():
      raise ValidationError("That email is already registered!")

  def check_username(self,field):
    if User.query.filter_by(username=field.data).first():
      raise ValidationError("That username is already registered!")