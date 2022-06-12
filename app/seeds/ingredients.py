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

    autumn_cheesecake_1 = Ingredient(
            amount=1, food_item='graham cracker crumbs', measurement_unit_id=1, recipe_id=2
        )

    autumn_cheesecake_2 = Ingredient(
            amount=0.5, food_item='finely chopped pecans', measurement_unit_id=1, recipe_id=2
        )

    autumn_cheesecake_3 = Ingredient(
            amount=3, food_item='white sugar', measurement_unit_id=12, recipe_id=2
        )

    autumn_cheesecake_4 = Ingredient(
            amount=0.5, food_item='ground cinnamon', measurement_unit_id=13, recipe_id=2
        )

    autumn_cheesecake_5 = Ingredient(
            amount=0.25, food_item='unsalted butter, melted', measurement_unit_id=1, recipe_id=2
        )

    autumn_cheesecake_6 = Ingredient(
            amount=16, food_item='cream cheese, softened', measurement_unit_id=7, recipe_id=2
        )

    autumn_cheesecake_7 = Ingredient(
            amount=0.5, food_item='white sugar', measurement_unit_id=1, recipe_id=2
        )

    autumn_cheesecake_8 = Ingredient(
            amount=2, food_item='eggs', measurement_unit_id=14, recipe_id=2
        )

    autumn_cheesecake_9 = Ingredient(
            amount=0.5, food_item='vanilla extract', measurement_unit_id=13, recipe_id=2
        )

    autumn_cheesecake_10 = Ingredient(
            amount=4, food_item='apples - peeled, cored and thinly sliced', measurement_unit_id=1, recipe_id=2
        )

    autumn_cheesecake_11 = Ingredient(
            amount=0.3, food_item='white sugar', measurement_unit_id=1, recipe_id=2
        )

    autumn_cheesecake_12 = Ingredient(
            amount=0.5, food_item='ground cinnamon', measurement_unit_id=13, recipe_id=2
        )

    autumn_cheesecake_13 = Ingredient(
            amount=0.25, food_item='chopped pecans', measurement_unit_id=1, recipe_id=2
        )
    
    db.session.add.all([
        Ingredient(
            amount=4, food_item='(1/2 pounds) rib-eye steaks, or steak of choice', measurement_unit_id=14, recipe_id=3
        ),
        Ingredient(
            amount=2, food_item='sea salt', measurement_unit_id=12, recipe_id=3
        ),
        Ingredient(
            amount=2, food_item='lemon pepper', measurement_unit_id=12, recipe_id=3
        ),
        Ingredient(
            amount=2, food_item='(12 fluid ounces) beer of choice', measurement_unit_id=15, recipe_id=3
        )
    ])

    db.session.add.all([
        Ingredient(
            amount=1, food_item='cubed seeded watermelon', measurement_unit_id=1, recipe_id=4
        ),
        Ingredient(
            amount=1.25, food_item='water', measurement_unit_id=1, recipe_id=4
        ),
        Ingredient(
            amount=3, food_item='sweetened strawberry lemonade drink mix', measurement_unit_id=12, recipe_id=4
        ),
    ])
    
    db.session.add.all([
        Ingredient(
            amount=0.5, food_item='panko bread crumbs', measurement_unit_id=1, recipe_id=5
        ),
        Ingredient(
            amount=0.3, food_item='Parmesan cheese', measurement_unit_id=1, recipe_id=5
        ),
        Ingredient(
            amount=0.25, food_item='paprika', measurement_unit_id=13, recipe_id=5
        ),
        Ingredient(
            amount=0.25, food_item='salt', measurement_unit_id=13, recipe_id=5
        ),
        Ingredient(
            amount=0.25, food_item='ground black pepper', measurement_unit_id=13, recipe_id=5
        ),
        Ingredient(
            amount=3, food_item='melted butter', measurement_unit_id=12, recipe_id=5
        ),
        Ingredient(
            amount=2, food_item='white wine (Optional)', measurement_unit_id=13, recipe_id=5
        ),
        Ingredient(
            amount=1, food_item='Dijon mustard', measurement_unit_id=13, recipe_id=5
        ),
        Ingredient(
            amount=1, food_item='clove garlic, crushed', measurement_unit_id=14, recipe_id=5
        ),
        Ingredient(
            amount=4, food_item='skinless, boneless chicken breast halves, pounded to an even thickness', measurement_unit_id=14, recipe_id=5
        )
    ])

    db.session.add.all([
        Ingredient(
            amount=16, food_item='linguine pasta', measurement_unit_id=7, recipe_id=6
        ),
        Ingredient(
            amount=4, food_item='butter', measurement_unit_id=12, recipe_id=6
        ),
        Ingredient(
            amount=2, food_item='cloves garlic, minced', measurement_unit_id=14, recipe_id=6
        ),
        Ingredient(
            amount=1, food_item=' jumbo shrimp, peeled and deveined', measurement_unit_id=10, recipe_id=6
        ),
        Ingredient(
            amount=2, food_item='Pinot Grigio wine', measurement_unit_id=12, recipe_id=6
        ),
        Ingredient(
            amount=2, food_item='lemon juice, or to taste', measurement_unit_id=13, recipe_id=6
        ),
        Ingredient(
            amount=0.5, food_item='half-and-half', measurement_unit_id=1, recipe_id=6
        ),
        Ingredient(
            amount=0.25, food_item='finely shredded Parmesan cheese', measurement_unit_id=1, recipe_id=6
        ),
        Ingredient(
            amount=2, food_item='chopped fresh parsley, or to taste', measurement_unit_id=12, recipe_id=6
        )
    ])

    db.session.add.all([
        Ingredient(
            amount=0.25, food_item='soy sauce', measurement_unit_id=1, recipe_id=7
        ),
        Ingredient(
            amount=2, food_item='sesame oil', measurement_unit_id=12, recipe_id=7
        ),
        Ingredient(
            amount=1, food_item='mirin (Japanese sweet wine)', measurement_unit_id=12, recipe_id=7
        ),
        Ingredient(
            amount=1, food_item='honey', measurement_unit_id=12, recipe_id=7
        ),
        Ingredient(
            amount=1, food_item='rice wine vinegar', measurement_unit_id=12, recipe_id=7
        ),
        Ingredient(
            amount=0.5, food_item='seasame seeds', measurement_unit_id=1, recipe_id=7
        ),
        Ingredient(
            amount=4, food_item='(6 ounce) tuna steaks', measurement_unit_id=14, recipe_id=7
        ),
        Ingredient(
            amount=1, food_item='olive oil', measurement_unit_id=12, recipe_id=7
        ),
        Ingredient(
            amount=1, food_item='wasabi taste', measurement_unit_id=14, recipe_id=7
        ),
    ])

    db.session.add.all([
        Ingredient(
            amount=8, food_item='cream cheese', measurement_unit_id=7, recipe_id=8
        ),
        Ingredient(
            amount=2, food_item='grated Parmesan cheese', measurement_unit_id=12, recipe_id=8
        ),
        Ingredient(
            amount=1.5, food_item='garlic powder', measurement_unit_id=13, recipe_id=8
        ),
        Ingredient(
            amount=1.5, food_item='shredded Cheddar cheese', measurement_unit_id=1, recipe_id=8
        ),
        Ingredient(
            amount=16, food_item='whole jalapeno peppers with stems', measurement_unit_id=14, recipe_id=8
        ),
        Ingredient(
            amount=8, food_item='slices bacon, cut in half crosswise', measurement_unit_id=16, recipe_id=8
        ),
    ])

    db.session.add.all([
        Ingredient(
            amount=1, food_item='finely chopped wakame', measurement_unit_id=12, recipe_id=9
        ),
        Ingredient(
            amount=4, food_item='water', measurement_unit_id=1, recipe_id=9
        ),
        Ingredient(
            amount=2, food_item='dashi granules', measurement_unit_id=13, recipe_id=9
        ),
        Ingredient(
            amount=3, food_item='miso paste', measurement_unit_id=12, recipe_id=9
        ),
        Ingredient(
            amount=4, food_item='tofu, cubed', measurement_unit_id=7, recipe_id=9
        ),
        Ingredient(
            amount=2, food_item='onions, sliced on the bias', measurement_unit_id=14, recipe_id=9
        ),
    ])

    db.session.add.all([
        Ingredient(
            amount=8, food_item='bacon', measurement_unit_id=16, recipe_id=10
        ),
        Ingredient(
            amount=4, food_item='shredded Swiss cheese', measurement_unit_id=7, recipe_id=10
        ),
        Ingredient(
            amount=2, food_item='butter, melted', measurement_unit_id=12, recipe_id=10
        ),
        Ingredient(
            amount=4, food_item='eggs', measurement_unit_id=14, recipe_id=10
        ),
        Ingredient(
            amount=0.25, food_item='finely chopped onion', measurement_unit_id=1, recipe_id=10
        ),
        Ingredient(
            amount=1, food_item='salt', measurement_unit_id=13, recipe_id=10
        ),
        Ingredient(
            amount=0.5, food_item='all-purpose flour', measurement_unit_id=1, recipe_id=10
        ),
        Ingredient(
            amount=1.5, food_item='milk', measurement_unit_id=1, recipe_id=10
        ),
    ])

        # Ingredient(
        #     amount=1, food_item='', measurement_unit_id=1, recipe_id=
        # ),


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

    db.session.add(autumn_cheesecake_1)
    db.session.add(autumn_cheesecake_2)
    db.session.add(autumn_cheesecake_3)
    db.session.add(autumn_cheesecake_4)
    db.session.add(autumn_cheesecake_5)
    db.session.add(autumn_cheesecake_6)
    db.session.add(autumn_cheesecake_7)
    db.session.add(autumn_cheesecake_8)
    db.session.add(autumn_cheesecake_9)
    db.session.add(autumn_cheesecake_10)
    db.session.add(autumn_cheesecake_11)
    db.session.add(autumn_cheesecake_12)
    db.session.add(autumn_cheesecake_13)

    db.session.commit()


def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
