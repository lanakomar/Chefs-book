from flask import Blueprint, jsonify, render_template, request
from flask_login import login_required
from app.models import db, User, Recipe, Instruction, Ingredient
from app.forms.recipe_form import RecipeForm


user_routes = Blueprint('users', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()

@user_routes.route('/<int:id>/recipes')
@login_required
def get_user_recipes(id):
    user = User.query.get(id)

    recipe_box = {recipe.id: recipe.to_dict() for recipe in user.recipes}

    return recipe_box


@user_routes.route('/<int:id>/recipes', methods=["GET", "POST"])
# @login_required
def create_recipe(id):
    '''
    Creates new recipe
    '''
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():
        print("!!! valid")
        recipe = Recipe(
            title = form.data['title'],
            time_to_cook = form.data['time_to_cook'],
            description = form.data['description'],
            img_url = form.data['img_url'],
            user_id = id,
            servings = form.data['servings']
        )
        instructions_data = form.data['instructions']
        ingredients_data = form.data['ingredient']
        for item in instructions_data:
            instruction = Instruction(
                specification = item['specification'],
                list_order = item['list_order']
            )
            recipe.instructions.append(instruction)

        for item in ingredients_data:
            ingredient = Ingredient(
                amount = item['amount'],
                food_item = item['food_item'],
                measurement_unit_id = item['measurement_unit_id']
            )
            recipe.ingredient.append(ingredient)


        db.session.add(recipe)
        db.session.commit()
        return recipe.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
