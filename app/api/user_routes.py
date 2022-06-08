from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import User

user_routes = Blueprint('users', __name__)


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
