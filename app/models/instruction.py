from .db import db


class Instruction(db.Model):
    __tablename__ = "instructions"

    id = db.Column(db.Integer, primary_key=True)
    specification = db.Column(db.Text, nullable=False)
    list_order = db.Column(db.Integer, nullable=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    recipe = db.relationship("Recipe", back_populates="instructions")


    def to_dict(self):
        return {
            'id': self.id,
            'specification': self.specification,
            'list_order': self.list_order,
            'recipe_id': self.recipe_id
        }
