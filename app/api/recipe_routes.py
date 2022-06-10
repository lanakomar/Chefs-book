from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.awsS3 import upload_base64_to_s3

from app.models import db, Recipe, Instruction, Ingredient
from app.forms.recipe_form import RecipeForm


recipe_routes = Blueprint('recipes', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@recipe_routes.route('')
def get_all_recipies():
    recipes = Recipe.query.all()
    return { recipe.id: recipe.to_dict() for recipe in recipes }


@recipe_routes.route('/<int:id>', methods=["PUT"])
@login_required
def edit_recipe(id):
    '''
    Creates new recipe
    '''
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():
        recipe = Recipe.query.get(id)
        if recipe:
            if form.data["image"]  != recipe.img_url:
                img_url = upload_base64_to_s3(form.data["image"])
            else:
                img_url = recipe.img_url
            recipe.title = form.data['title'],
            recipe.time_to_cook = form.data['time_to_cook'],
            recipe.description = form.data['description'],
            recipe.img_url = img_url,
            recipe.user_id = current_user.id,
            recipe.servings = form.data['servings']

            instructions_data = form.data['instructions']
            ingredients_data = form.data['ingredient']
            print("************")
            print(instructions_data)
            print("**********")
            print(ingredients_data)
            print("*************")
            recipe.instructions = []
            for item in instructions_data:
                instruction = Instruction.query.get(item['id'])
                instruction.specification = item['specification']
                instruction.list_order = item['list_order']

                recipe.instructions.append(instruction)

            recipe.ingredient = []
            for item in ingredients_data:
                ingredient = Ingredient.query.get(item['id'])
                ingredient.amount = item['amount']
                ingredient.food_item = item['food_item']
                ingredient.measurement_unit_id = item['measurement_unit_id']

                recipe.ingredient.append(ingredient)

            print("===================")
            print(recipe)
            # db.session.add(recipe)
            # db.session.commit()
            # return recipe.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
