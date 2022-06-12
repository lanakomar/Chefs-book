from wtforms import StringField, IntegerField, FloatField, BooleanField, Form
from wtforms.validators import DataRequired, Length

class IngredientForm(Form):
    amount = FloatField("amount", validators=[DataRequired(message="This field is required.")])
    food_item = StringField("food_item",validators=[DataRequired(message="This field is required."),\
                                           Length(max=500, message="The food item should be less than 500 characters.")])
    measurement_unit_id = IntegerField("measurement_unit_id", validators=[DataRequired(message="This field is required.")])
    identifier = IntegerField("identifier")
class IngredientDeletedForm(Form):
    identifier = IntegerField("identifier")
