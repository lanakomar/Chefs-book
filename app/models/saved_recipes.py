from .db import db

saved_recipes = db.Table(
    "saved_recipes",
    db.Column("user_id", db.Integer, db.ForeignKey(
        "users.id"), primary_key=True),
    db.Column("recipe_id", db.Integer, db.ForeignKey(
        "recipes.id"), primary_key=True)
)
