from wtforms import TextAreaField, IntegerField, Form
from wtforms.validators import DataRequired

class InstructionForm(Form):
    specification = TextAreaField("specification", validators=[DataRequired(message="This field is required.")])
    list_order = IntegerField("list_order", validators=[DataRequired(message="This field is required.")])
    # recipe_id = IntegerField("recipe_id", validators=[DataRequired(message="This field is required.")])
