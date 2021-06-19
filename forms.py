from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Optional, URL, NumberRange

class CupcakeForm(FlaskForm):
    """ Form to add a new pet """
    flavor = StringField("Flavor", validators=[
                       InputRequired(message="Flavor can't be blank")])
    size = SelectField("Size", choices=[
                            ('small', 'small'), ('medium', 'medium'), ('large', 'large')],
                            validators=[
                            InputRequired(message="Must select a size")])
    rating = FloatField("Rating", validators=[
                        NumberRange(min=0, max=10)])
    image = StringField("Cupcake photo URL", validators=[Optional(),
                        URL(message="Must be a vaild URL")])