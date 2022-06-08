from app.models import db, Instruction


def seed_instructions():
    crab_cheddar_quiche_1 = Instruction(
        specification="Preheat oven to 350 degrees F (175 degrees C).", list_order=1, recipe_id=1
    )

    crab_cheddar_quiche_2 = Instruction(
        specification="Beat eggs, mayonnaise, milk, flour, and 1 teaspoon seafood seasoning in a bowl until smooth and creamy; stir Cheddar cheese and parsley into egg mixture. Gently fold crabmeat into the filling.",\
        list_order=2, recipe_id=1
    )

    crab_cheddar_quiche_3 = Instruction(
        specification="Pour crabmeat filling into the pie crust. Sprinkle a pinch of seafood seasoning over the quiche.",\
        list_order=3, recipe_id=1
    )

    crab_cheddar_quiche_4 = Instruction(
        specification="Bake in the preheated oven until a knife inserted into the center of the quiche comes out clean and the top is lightly browned, 40 to 45 minutes.",\
        list_order=4, recipe_id=1
    )

    db.session.add(crab_cheddar_quiche_1)
    db.session.add(crab_cheddar_quiche_2)
    db.session.add(crab_cheddar_quiche_3)
    db.session.add(crab_cheddar_quiche_4)

    db.session.commit()


def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()
