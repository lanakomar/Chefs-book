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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
        Ingredient(
            amount=1.5, food_item='beef top sirloin, thinly sliced', measurement_unit_id=10, recipe_id=11
        ),
        Ingredient(
            amount=0.3, food_item='white sugar', measurement_unit_id=1, recipe_id=11
        ),
        Ingredient(
            amount=2, food_item='frozen orange juice concentrate', measurement_unit_id=12, recipe_id=11
        ),
        Ingredient(
            amount=1, food_item='salt', measurement_unit_id=13, recipe_id=11
        ),
        Ingredient(
            amount=1, food_item='soy sauce', measurement_unit_id=12, recipe_id=11
        ),
        Ingredient(
            amount=1, food_item='long grain rice', measurement_unit_id=1, recipe_id=11
        ),
        Ingredient(
            amount=2, food_item='water', measurement_unit_id=1, recipe_id=11
        ),
        Ingredient(
            amount=0.25, food_item='cornstarch', measurement_unit_id=1, recipe_id=11
        ),
        Ingredient(
            amount=2, food_item='orange zest', measurement_unit_id=13, recipe_id=11
        ),
        Ingredient(
            amount=3, food_item='grated fresh ginger', measurement_unit_id=12, recipe_id=11
        ),
        Ingredient(
            amount=1.5, food_item='minced garlic', measurement_unit_id=12, recipe_id=11
        ),
        Ingredient(
            amount=8, food_item='broccoli florets, lightly steamed or blanched', measurement_unit_id=14, recipe_id=11
        ),
        Ingredient(
            amount=2, food_item='2 cups oil for frying', measurement_unit_id=1, recipe_id=11
        )
    ])

    db.session.add_all([
        Ingredient(
            amount=18, food_item='whole graham crackers', measurement_unit_id=14, recipe_id=12
        ),
        Ingredient(
            amount=113, food_item='unsalted butter (1 stick), melted', measurement_unit_id=4, recipe_id=12
        ),
        Ingredient(
            amount=2, food_item='granulated sugar', measurement_unit_id=12, recipe_id=12
        ),
        Ingredient(
            amount=0.25, food_item='salt', measurement_unit_id=13, recipe_id=12
        ),
        Ingredient(
            amount=1, food_item='semisweet chocolate, finely chopped', measurement_unit_id=10, recipe_id=12
        ),
        Ingredient(
            amount=3, food_item='cold heavy cream, plus more for serving', measurement_unit_id=1, recipe_id=12
        ),
        Ingredient(
            amount=2, food_item='instant espresso powder', measurement_unit_id=13, recipe_id=12
        ),
        Ingredient(
            amount=0.5, food_item='salt', measurement_unit_id=13, recipe_id=12
        ),
        Ingredient(
            amount=1, food_item='pure vanilla extract', measurement_unit_id=12, recipe_id=12
        )
    ])

    db.session.add_all([
        Ingredient(
            amount=3, food_item='cubed watermelon', measurement_unit_id=1, recipe_id=13
        ),
        Ingredient(
            amount=2, food_item='large ripe tomatoes', measurement_unit_id=14, recipe_id=13
        ),
        Ingredient(
            amount=1, food_item='medium cucumber', measurement_unit_id=14, recipe_id=13
        ),
        Ingredient(
            amount=1, food_item='small red onion', measurement_unit_id=14, recipe_id=13
        ),
        Ingredient(
            amount=0.3, food_item='pitted kalamata olives', measurement_unit_id=1, recipe_id=13
        ),
        Ingredient(
            amount=0.3, food_item='crumbled feta', measurement_unit_id=1, recipe_id=13
        ),
        Ingredient(
            amount=1, food_item='', measurement_unit_id=1, recipe_id=13
        ),
        Ingredient(
            amount=1, food_item='', measurement_unit_id=1, recipe_id=13
        ),
    ])

    db.session.add_all([
        Ingredient(
            amount=4, food_item='ears fresh corn, shucked', measurement_unit_id=14, recipe_id=14
        ),
        Ingredient(
            amount=1, food_item='unsalted butter, at room temperature', measurement_unit_id=12, recipe_id=14
        ),
        Ingredient(
            amount=1, food_item='lemon, zested and cut into wedges, for serving', measurement_unit_id=14, recipe_id=14
        ),
        Ingredient(
            amount=0.25, food_item='teaspoon Old Bay seasoning, plus more for serving', measurement_unit_id=13, recipe_id=14
        )
    ])

    db.session.add_all([
        Ingredient(
            amount=4, food_item='bacon, chopped', measurement_unit_id=7, recipe_id=15
        ),
        Ingredient(
            amount=1, food_item='all-purpose flour', measurement_unit_id=1, recipe_id=15
        ),
        Ingredient(
            amount=0.5, food_item='salt', measurement_unit_id=13, recipe_id=15
        ),
        Ingredient(
            amount=0.25, food_item='freshly ground black pepper', measurement_unit_id=13, recipe_id=15
        ),
        Ingredient(
            amount=0.25, food_item='baking powder', measurement_unit_id=13, recipe_id=15
        ),
        Ingredient(
            amount=8, food_item='large eggs', measurement_unit_id=14, recipe_id=15
        ),
        Ingredient(
            amount=0.75, food_item='whole milk', measurement_unit_id=1, recipe_id=15
        ),
        Ingredient(
            amount=0.25, food_item='grated Parmesan', measurement_unit_id=1, recipe_id=15
        ),
        Ingredient(
            amount=0.25, food_item='chopped chives', measurement_unit_id=1, recipe_id=15
        ),
        Ingredient(
            amount=4, food_item='unsalted butter', measurement_unit_id=12, recipe_id=15
        ),
        Ingredient(
            amount=1, food_item='8- to 10-ounce) wheel of Camembert, rind on and cut into 1/4-inch slices (not wedges)', measurement_unit_id=14, recipe_id=15
        )
    ])

    db.session.add_all([
        Ingredient(
            amount=1, food_item='medium onion, any kind (except sweet), coarsely chopped ', measurement_unit_id=14, recipe_id=16
        ),
        Ingredient(
            amount=4, food_item='ground beef', measurement_unit_id=7, recipe_id=16
        ),
        Ingredient(
            amount=4, food_item='ground pork', measurement_unit_id=7, recipe_id=16
        ),
        Ingredient(
            amount=2, food_item='coarsely ground black pepper', measurement_unit_id=13, recipe_id=16
        ),
        Ingredient(
            amount=1.5, food_item='salt', measurement_unit_id=13, recipe_id=16
        ),
        Ingredient(
            amount=8, food_item='plain kefir, plus more as needed', measurement_unit_id=7, recipe_id=16
        ),
        Ingredient(
            amount=4, food_item='all-purpose flour, plus more for dusting (if needed)', measurement_unit_id=1, recipe_id=16
        ),
        Ingredient(
            amount=1, food_item='fine salt', measurement_unit_id=13, recipe_id=16
        ),
        Ingredient(
            amount=1, food_item='plus 1 tablespoon cold water', measurement_unit_id=1, recipe_id=16
        ),
        Ingredient(
            amount=8, food_item='Peanut oil or refined sunflower oil, for frying', measurement_unit_id=1, recipe_id=16
        ),
    ])

    db.session.add_all([
        Ingredient(
            amount=4, food_item='(8-ounce) center-cut pork chops, about 1/2-inch thick', measurement_unit_id=14, recipe_id=17
        ),
        Ingredient(
            amount=1, food_item='salt', measurement_unit_id=8, recipe_id=17
        ),
        Ingredient(
            amount=1, food_item='black pepper', measurement_unit_id=8, recipe_id=17
        ),
        Ingredient(
            amount=2, food_item='eggs, beaten', measurement_unit_id=14, recipe_id=17
        ),
        Ingredient(
            amount=0.5, food_item='milk', measurement_unit_id=1, recipe_id=17
        ),
        Ingredient(
            amount=1, food_item='cayenne powder', measurement_unit_id=8, recipe_id=17
        ),
        Ingredient(
            amount=3, food_item='fresh bread crumbs (from 8 slices crustless day-old sandwich bread)', measurement_unit_id=1, recipe_id=17
        ),
        Ingredient(
            amount=1, food_item='clarified butter, extra-virgin olive oil or lard, plus more as needed', measurement_unit_id=1, recipe_id=17
        ),
    ])

    db.session.add_all([
        Ingredient(
            amount=1, food_item='large egg', measurement_unit_id=14, recipe_id=18
        ),
        Ingredient(
            amount=1, food_item='egg yolk', measurement_unit_id=14, recipe_id=18
        ),
        Ingredient(
            amount=2.5, food_item='baking powder', measurement_unit_id=12, recipe_id=18
        ),
        Ingredient(
            amount=2, food_item='granulated sugar', measurement_unit_id=12, recipe_id=18
        ),
        Ingredient(
            amount=1, food_item='salt', measurement_unit_id=13, recipe_id=18
        ),
        Ingredient(
            amount=1.25, food_item='whole milk', measurement_unit_id=1, recipe_id=18
        ),
        Ingredient(
            amount=1, food_item='all-purpose flour', measurement_unit_id=1, recipe_id=18
        ),
        Ingredient(
            amount=1, food_item='plus 2 tablespoons clarified butter (or store-bought), melted', measurement_unit_id=1, recipe_id=18
        ),
    ])

    db.session.add_all([
        Ingredient(
            amount=1.5, food_item='zucchini, thinly sliced', measurement_unit_id=10, recipe_id=19
        ),
        Ingredient(
            amount=4, food_item='eggs', measurement_unit_id=14, recipe_id=19
        ),
        Ingredient(
            amount=2.5, food_item='milk or half-and-half', measurement_unit_id=1, recipe_id=19
        ),
        Ingredient(
            amount=1, food_item='grated nutmeg', measurement_unit_id=8, recipe_id=19
        ),
        Ingredient(
            amount=1, food_item='chopped thyme', measurement_unit_id=13, recipe_id=19
        ),
        Ingredient(
            amount=2, food_item='butter for greasing baking dish', measurement_unit_id=12, recipe_id=19
        ),
        Ingredient(
            amount=2, food_item='grated cheese, such as Gruyère or Cheddar', measurement_unit_id=7, recipe_id=19
        ),
    ])

    db.session.add_all([
        Ingredient(
            amount=6, food_item='large egg whites, room temperature', measurement_unit_id=14, recipe_id=20
        ),
        Ingredient(
            amount=1.5, food_item='granulated sugar', measurement_unit_id=1, recipe_id=20
        ),
        Ingredient(
            amount=2, food_item='corn starch', measurement_unit_id=13, recipe_id=20
        ),
        Ingredient(
            amount=0.5, food_item='lemon juice', measurement_unit_id=12, recipe_id=20
        ),
        Ingredient(
            amount=0.5, food_item='vanilla extract', measurement_unit_id=12, recipe_id=20
        ),
        Ingredient(
            amount=1.5, food_item='heavy whipping cream, (very cold)', measurement_unit_id=1, recipe_id=20
        ),
        Ingredient(
            amount=2, food_item='granulated sugar', measurement_unit_id=12, recipe_id=20
        ),
        Ingredient(
            amount=5, food_item='fresh fruit, blueberries, kiwi, raspberries, sliced strawberries, etc', measurement_unit_id=1, recipe_id=20
        ),
        Ingredient(
            amount=15, food_item='Mint leaves , for garnish, optional', measurement_unit_id=14, recipe_id=20
        ),
    ])

    # db.session.add_all([
    #     Ingredient(
    #         amount=1, food_item='', measurement_unit_id=1, recipe_id=
    #     ),
    # ])


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
