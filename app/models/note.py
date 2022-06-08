from .db import db
from datetime import datetime


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.Date, nullable=False, default=datetime.now().date())

    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.id"), nullable=False)
    recipe = db.relationship("Recipe", back_populates="notes")

    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    author = db.relationship("User", back_populates="notes")


    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'date_created': self.date_created,
            'recipe_id': self.recipe_id,
            'author_id': self.author_id
        }
