from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import NumberRange

class ResultForm(FlaskForm):
	num_fizz = IntegerField('Fizz Number:', validators=[NumberRange(min=1, max=100)])
	num_buzz = IntegerField('Bizz Number:', validators=[NumberRange(min=1, max=100)])
	submit = SubmitField('View Results')
