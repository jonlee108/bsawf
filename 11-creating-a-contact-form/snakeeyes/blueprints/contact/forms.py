from flask_wtf import Form
from wtforms import TextAreaField, RadioField
from wtforms_components import EmailField
from wtforms.validators import DataRequired, Length


class ContactForm(Form):
    email = EmailField("What's your e-mail address?",
                    [DataRequired(), Length(3, 254)])
    message = TextAreaField("What's your question or issue?",
                    [DataRequired(), Length(1, 8192)])

class FeedbackForm(Form):    
    email = EmailField("What's your e-mail address?",
                    [DataRequired(), Length(3, 254)])
    message = TextAreaField("What feedback would you like to share with us?",
                    [DataRequired(), Length(1, 8192)])


    nps_choices = [(str(x),str(x)) for x in range(1,11)]
    nps_label = "On a scale from 1 to 10 how happy are you with the product?"
    nps = RadioField(label=nps_label,
                    choices=nps_choices,
                    validators=[DataRequired()])