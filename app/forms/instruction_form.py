from wtforms import TextAreaField, IntegerField, BooleanField, Form
from wtforms.validators import InputRequired

class InstructionForm(Form):
    specification = TextAreaField("specification", validators=[InputRequired(message="This field is required.")])
    list_order = IntegerField("list_order", validators=[InputRequired(message="This field is required.")])
    identifier = IntegerField("identifier")

class InstructionDeletedForm(Form):
    identifier = IntegerField("identifier")
