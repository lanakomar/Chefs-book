from .db import db


class Recipe(db.Model):
    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    time_to_cook = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(500), nullable=False)


    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = db.relationship("User", back_populates="recipes")

    instructions = db.relationship("Instruction", back_populates="recipe", cascade="all, delete-orphan")

    notes = db.relationship("Note", back_populates="recipe", cascade="all, delete-orphan")

    ingredient = db.relationship("Ingredient", back_populates="recipe", cascade="all, delete-orphan")


    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'time_to_cook': self.time_to_cook,
            'description': self.description,
            'servings': self.servings,
            'img_url': self.img_url,
            'user_id': self.user_id,
            'instructions': {instruction.id: instruction.to_dict() for instruction in self.instructions},
            'notes': {note.id: note.to_dict() for note in self.notes},
            'ingredients': {ingredient.id: ingredient.to_dict() for ingredient in self.ingredient}
        }
