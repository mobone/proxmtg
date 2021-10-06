from flask_wtf import Form
from wtforms.fields import *
from wtforms.validators import Required, Email


class SignupForm(Form):
    deck_name = TextField("Deck Name")
    card_input = TextAreaField(u'Cards')
    

    submit = SubmitField(u'Get Images')
