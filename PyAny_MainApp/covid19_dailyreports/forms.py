from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email

class HealthChecklistForm(FlaskForm):  
  full_name = StringField('Firstname MiddleInitial Lastname',validators=[DataRequired()])
  address = TextAreaField('Full Address',validators=[DataRequired()])
  gender = StringField('Gender',validators=[DataRequired()])
  birthdate = DateField('Birthdate',validators=[DataRequired()])
  temperature = FloatField('Temp. (Celsius)',validators=[DataRequired()])
  mobile_number = IntegerField('Mobile Number')
  email = StringField('Email',validators=[Email()])
  submit = SubmitField('Submit')