from .db import db

grocery_lists = db.Table(
    "grocery_lists",
    db.Column("user_id", db.Integer, db.ForeignKey(
        "users.id"), primary_key=True),
    db.Column("ingredient_id", db.Integer, db.ForeignKey(
        "ingredients.id"), primary_key=True)
)
