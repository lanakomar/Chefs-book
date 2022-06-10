from .db import db
from .grocery_list import grocery_lists


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(5, 2), nullable=False)
    food_item = db.Column(db.String(500), nullable=False)

    measurement_unit_id = db.Column(db.Integer, db.ForeignKey("measurement_units.id"), nullable=False)
    measurement_unit = db.relationship("Measurement_unit", back_populates="ingredient")

    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    recipe = db.relationship("Recipe", back_populates="ingredient")

    shoppers = db.relationship("User", back_populates="ingredients_to_buy", secondary=grocery_lists)


    def to_dict(self):
        return {
            'id': self.id,
            'amount': float(self.amount),
            'food_item': self.food_item,
            'measurement_unit_id': self.measurement_unit.name,
            'recipe_id': self.recipe_id,
            'shoppers': [shopper.id for shopper in self.shoppers]
        }
