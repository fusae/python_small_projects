from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class guessBookForm(Form):
    name = TextField('Name', validators=[DataRequired('Please enter your name')])
    message = TextAreaField('Message', validators=[DataRequired('Please enter a message')])
    submit = SubmitField('submit')
