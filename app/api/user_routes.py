from crypt import methods
from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.awsS3 import upload_base64_to_s3
from app.models import db, User, Recipe, Instruction, Ingredient, recipe
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


@user_routes.route('/<int:id>/recipes', methods=["POST"])
@login_required
def create_recipe(id):
    '''
    Creates new recipe
    '''
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():

        img_url = upload_base64_to_s3(form.data["image"])

        recipe = Recipe(
            title = form.data['title'],
            time_to_cook = form.data['time_to_cook'],
            description = form.data['description'],
            img_url = img_url,
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



@user_routes.route('/<int:id>/groceries', methods=["POST"])
@login_required
def add_groceries(id):
    '''
    Adds items to user's Grocery List
    '''
    user = User.query.get(id)

    item_ids = request.get_json()
    added_items = []
    for idx in item_ids:
        item = Ingredient.query.get(idx)
        user.ingredients_to_buy.append(item)
        added_items.append(item.to_dict())

    db.session.add(user)
    db.session.commit()

    return jsonify(added_items)


@user_routes.route('/<int:id>/groceries', methods=["DELETE"])
@login_required
def delete_grocery_items(id):
    '''
    Deletes items from user's Grocery List
    '''

    user = User.query.get(id)

    item_ids = request.get_json()
    for idx in item_ids:
        item = Ingredient.query.get(idx)
        user.ingredients_to_buy.remove(item)

    db.session.commit()

    return {'message': "success"}


@user_routes.route('/<int:id>/saved-recipes', methods=["POST"])
@login_required
def save_to_recipe_box(id):
    '''
    Saves recipe to recipe box
    '''
    user = User.query.get(id)
    recipe_id = request.get_json()
    recipe_to_add = Recipe.query.get(recipe_id)
    if recipe_to_add:
        user.recipes_saved.append(recipe_to_add)
        db.session.add(user)
        db.session.commit()
    else:
        return {'errors': ['Recipe not found.']}, 404
    return recipe_to_add.to_dict()


@user_routes.route('/<int:id>/saved-recipes', methods=["DELETE"])
@login_required
def delete_from_recipe_box(id):
    '''
    Deletes saved recipe from recipe box
    '''
    user = User.query.get(id)
    recipe_id = request.get_json()
    recipe_to_delete = Recipe.query.get(recipe_id)
    if recipe_to_delete:
        user.recipes_saved.remove(recipe_to_delete)
        db.session.add(user)
        db.session.commit()
    else:
        return {'errors': ['Recipe not found.']}, 404
    return {'message': "success"}
