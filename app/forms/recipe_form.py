from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.fields import FormField, FieldList
from wtforms.validators import DataRequired, Length
from app.forms.instruction_form import InstructionForm
from app.forms.ingredient_form import IngredientForm


class RecipeForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(message="This field is required."),\
                                          Length(max=255, message="The title should be less than 255 characters.")])
    time_to_cook = StringField("time_to_cook", validators=[DataRequired(message="This field is required."),\
                                          Length(max=250, message="Time to cook should be less than 50 characters.")])
    description = TextAreaField("description", validators=[DataRequired(message="This field is required.")])
    img_url = StringField("img_url", validators=[DataRequired(message="This field is required.")])
    servings = IntegerField("servings", validators=[DataRequired(message="This field is required.")])
    ingredient = FieldList(FormField(IngredientForm), min_entries=1)
    instructions = FieldList(FormField(InstructionForm), min_entries=1)
