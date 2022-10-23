from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()])
    year = IntegerField('Year: ', validators=[DataRequired()])
    origin = StringField('Origin: ',  validators=[DataRequired()])
    mpg = IntegerField('MPG: ',  validators=[DataRequired()])
    submit = SubmitField('Save')
class SearchForm(FlaskForm):
    name = StringField('Name of Car Brand: ', validators=[DataRequired()])
    submit = SubmitField('Search')