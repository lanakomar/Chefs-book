from .db import db
from .grocery_list import grocery_lists
from .saved_recipes import saved_recipes

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    # one - many relationship with Recipe
    recipes = db.relationship("Recipe", back_populates="user")

    # one - many with Note
    notes = db.relationship("Note", back_populates="author")

    #many - many with Ingredient (Grocery_list)
    ingredients_to_buy = db.relationship("Ingredient", back_populates="shoppers", secondary=grocery_lists)

    #many - many with Recipe (saved_recipes)
    recipes_saved = db.relationship("Recipe", back_populates="users_saved", secondary=saved_recipes)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'grocery_list': [ingredient.to_dict() for ingredient in self.ingredients_to_buy],
            'recipes_saved': {recipe.id: recipe.to_dict() for recipe in self.recipes_saved}
        }
