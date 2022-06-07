from app.models import db, Ingredient


def seed_ingredients():
    crab_cheddar_quiche_1 = Ingredient(
        amount=1, food_item='(9 inch) unbaked pie crust',\
        measurement_unit_id=14, recipe_id=1
    )

    crab_cheddar_quiche_2 = Ingredient(
        amount=3, food_item='eggs', measurement_unit_id=14, recipe_id=1
    )

    crab_cheddar_quiche_3 = Ingredient(
        amount=0.5, food_item='mayonnaise', measurement_unit_id=1, recipe_id=1
    )

    crab_cheddar_quiche_4 = Ingredient(
            amount=0.5, food_item='whole milk', measurement_unit_id=1, recipe_id=1
        )

    crab_cheddar_quiche_5 = Ingredient(
            amount=2, food_item='all-purpose flour', measurement_unit_id=12, recipe_id=1
        )

    crab_cheddar_quiche_6 = Ingredient(
            amount=1, food_item='seafood seasoning', measurement_unit_id=13, recipe_id=1
        )

    crab_cheddar_quiche_7 = Ingredient(
            amount=1, food_item='shredded Cheddar cheese', measurement_unit_id=1, recipe_id=1
        )

    crab_cheddar_quiche_8 = Ingredient(
            amount=0.5, food_item='chopped fresh parsley', measurement_unit_id=1, recipe_id=1
        )

    crab_cheddar_quiche_9 = Ingredient(
            amount=1, food_item='crabmeat', measurement_unit_id=1, recipe_id=1
        )

    crab_cheddar_quiche_10 = Ingredient(
            amount=1, food_item='seafood seasoning', measurement_unit_id=8, recipe_id=1
        )


    db.session.add(crab_cheddar_quiche_1)
    db.session.add(crab_cheddar_quiche_2)
    db.session.add(crab_cheddar_quiche_3)
    db.session.add(crab_cheddar_quiche_4)
    db.session.add(crab_cheddar_quiche_5)
    db.session.add(crab_cheddar_quiche_6)
    db.session.add(crab_cheddar_quiche_7)
    db.session.add(crab_cheddar_quiche_8)
    db.session.add(crab_cheddar_quiche_9)
    db.session.add(crab_cheddar_quiche_10)

    db.session.commit()


def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
