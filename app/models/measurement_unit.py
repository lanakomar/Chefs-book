from .db import db


class Measurement_unit(db.Model):
    __tablename__ = "measurement_units"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)


    ingredient = db.relationship("Ingredient", back_populates="measurement_unit")
