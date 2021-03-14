from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FlamesForm(FlaskForm):  
  your_name = StringField("Your name",validators=[DataRequired()])
  crush_name = StringField("Crush's name",validators=[DataRequired()])
  submit = SubmitField("Matchmake!")