"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, AnyOf, Optional, URL



class AddPetForm(FlaskForm):
    """ Form for adding pets """

    name = StringField("Pet Name", validators=[InputRequired()])

    species = StringField("Species", validators=[AnyOf(['cat', 'dog', 'porcupine'],),
                                                 InputRequired()])

    photo_url = StringField("Pet Photo", validators=[Optional(), URL()])

    age = SelectField('Age',
         choices= [('baby', 'Baby'),('young', 'Young'),
                   ('adult', 'Adult'),('senior', 'Senior')],
                   validators=[AnyOf(['baby', 'young', 'adult', 'senior',])])

    notes = TextAreaField("Notes")