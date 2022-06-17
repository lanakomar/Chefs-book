from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.fields import FormField, FieldList
from wtforms.validators import DataRequired, Length, ValidationError
from app.forms.instruction_form import InstructionForm, InstructionDeletedForm
from app.forms.ingredient_form import IngredientForm, IngredientDeletedForm
import re



def is_correct_input(form, field):
    expression = field.data
    reg = "(0?[0-9]|[1-5][0-9]) (hours?|minutes?|mins?)$"

    # compiling regex
    pattern = re.compile(reg)

    # searching regex
    match = re.search(pattern, expression)

    # validating conditions
    if not match:
        raise ValidationError("Invalid format, i.e. '1 hour'")

class RecipeForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(message="This field is required."),\
                                          Length(max=255, message="The title should be less than 255 characters.")])
    time_to_cook = StringField("time_to_cook", validators=[DataRequired(message="This field is required."),\
                                          Length(max=250, message="Time to cook should be less than 50 characters."),\
                                              is_correct_input])
    description = TextAreaField("description", validators=[DataRequired(message="This field is required.")])
    servings = IntegerField("servings", validators=[DataRequired(message="This field is required.")])
    ingredient = FieldList(FormField(IngredientForm), min_entries=1)
    ingredient_deleted = FieldList(FormField(IngredientDeletedForm))
    instructions = FieldList(FormField(InstructionForm), min_entries=1)
    instructions_deleted = FieldList(FormField(InstructionDeletedForm))
    image = TextAreaField("image", validators=[DataRequired(message="This image is required.")])
