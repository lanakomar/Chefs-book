from flask import Blueprint, jsonify
from app.models import Recipe


recipe_routes = Blueprint('recipes', __name__)

@recipe_routes.route('')
def get_all_recipies():
    recipes = Recipe.query.all()
    return { recipe.id: recipe.to_dict() for recipe in recipes }
