from flask.ext.wtf import Form
from wtforms import TextAreaField, BooleanField
from wtforms.validators import Required

class Questions(Form):
    question = TextAreaField('question', validators = [Required()])
    answer   = TextAreaField('answer',   validators = [Required()])
