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

    autumn_cheescake_1 = Instruction(
        specification="Preheat oven to 350 degrees F (175 degrees C). In a large bowl, stir together the graham cracker crumbs, 1/2 cup finely chopped pecans, 3 tablespoons sugar, 1/2 teaspoon cinnamon and melted butter; press into the bottom of a 9 inch springform pan. Bake in preheated oven for 10 minutes.",\
        list_order=1, recipe_id=2
    )

    autumn_cheescake_2 = Instruction(
        specification="In a large bowl, combine cream cheese and 1/2 cup sugar. Mix at medium speed until smooth. Beat in eggs one at a time, mixing well after each addition. Blend in vanilla; pour filling into the baked crust.",\
        list_order=2, recipe_id=2
    )

    autumn_cheescake_3 = Instruction(
        specification="In a small bowl, stir together 1/3 cup sugar and 1/2 teaspoon cinnamon. Toss the cinnamon-sugar with the apples to coat. Spoon apple mixture over cream cheese layer and sprinkle with 1/4 cup chopped pecans.",\
        list_order=3, recipe_id=2
    )

    autumn_cheescake_4 = Instruction(
        specification="Bake in preheated oven for 60 to 70 minutes. With a knife, loosen cake from rim of pan. Let cool, then remove the rim of pan. Chill cake before serving.",\
        list_order=4, recipe_id=2
    )

    db.session.add.all([
        Instruction(
            specification="Place the steaks in a large, shallow container with a lid. Season each side of the steaks with the salt and lemon pepper. Gently pour the beer over the steaks (making sure the seasoning doesn't wash off). Cover, and refrigerate for 1 to 2 hours.",\
            list_order=1, recipe_id=3
        ),
        Instruction(
            specification="Preheat grill for high heat.",\
            list_order=2, recipe_id=3
        ),
        Instruction(
            specification="Lightly oil grill grate. Place steaks on grill, and discard beer marinade. Cook for 5 minutes per side, or to desired doneness.",\
            list_order=3, recipe_id=3
        )
    ])

    db.session.add.all([
        Instruction(
            specification="Place the watermelon pieces onto a plastic-wrapped baking sheet, and freeze until solid, about 45 minutes.",\
            list_order=1, recipe_id=4
        ),
        Instruction(
            specification="Place the frozen watermelon, water, and strawberry lemonade drink mix in a blender; blend until slushy.",\
            list_order=2, recipe_id=4
        ),
    ])

    db.session.add.all([
        Instruction(
            specification="Preheat oven to 400 degrees F (200 degrees C). Line a baking sheet with aluminum foil and spray with cooking spray.",\
            list_order=1, recipe_id=5
        ),
        Instruction(
            specification="Whisk bread crumbs, Parmesan cheese, paprika, salt, and black pepper together in a shallow bowl. Stir butter, white wine, mustard, and garlic together in another bowl.",\
            list_order=2, recipe_id=5
        ),
        Instruction(
            specification="Dip each chicken breast half into melted butter mixture; press into bread crumb mixture to evenly coat. Place breaded chicken in a single layer on the prepared baking sheet. Pat any leftover bread crumb mixture onto chicken breasts.",\
            list_order=3, recipe_id=5
        ),
        Instruction(
            specification="Bake chicken in the preheated oven until no longer pink in the center and the juices run clear, about 20 minutes. An instant-read thermometer inserted into the center should read at least 165 degrees F (74 degrees C).",\
            list_order=4, recipe_id=5
        ),
    ])

    db.session.add.all([
        Instruction(
            specification="Bring a large pot of lightly salted water to a boil. Cook linguine at a boil until tender yet firm to the bite, about 8 minutes.",\
            list_order=1, recipe_id=6
        ),
        Instruction(
            specification="While pasta cooks, melt 2 tablespoons butter in a skillet over medium heat. Add garlic and cook until fragrant and lightly browned, about 1 minute. Add shrimp and cook until tails start curling in, about 2 minutes per side. Add remaining butter, Pinot Grigio, lemon juice, half-and-half, and Parmesan cheese. Stir to incorporate.",\
            list_order=2, recipe_id=6
        ),
        Instruction(
            specification="Drain linguine and divide noodles between 2 bowls. Serve shrimp mixture on top and garnish with parsley.",\
            list_order=3, recipe_id=6
        ),
    ])

    db.session.add.all([
    Instruction(
        specification="Stir together soy sauce, sesame oil, mirin, and honey in a small bowl. Pour half into a separate small bowl, stir in rice wine vinegar, and set it aside as a dipping sauce.",\
        list_order=1, recipe_id=7
    ),
    Instruction(
        specification="Spread sesame seeds out on a plate. Coat tuna steaks with remaining soy sauce mixture, then press into sesame seeds to coat.",\
        list_order=2, recipe_id=7
    ),
    Instruction(
        specification="Heat olive oil in a cast iron skillet over high heat until very hot. Place steaks in the pan; sear for about 30 seconds on each side. Serve with dipping sauce and wasabi paste.",\
        list_order=3, recipe_id=7
    ),
])

    db.session.add.all([
    Instruction(
        specification="Preheat an outdoor grill for medium heat, and lightly oil the grate.",\
        list_order=1, recipe_id=8
    ),
    Instruction(
        specification="Mix together the cream cheese, Parmesan cheese, garlic powder, and Cheddar cheese in a bowl until the mixture is thoroughly blended.",\
        list_order=2, recipe_id=8
    ),
    Instruction(
        specification="Lay a jalapeno pepper onto a work surface, and cut a lengthwise sliver from the side of the pepper, exposing the seeds and white membrane. With the handle of a teaspoon, scrape out the seeds and membrane, leaving the hollow pepper. Repeat for the rest of the peppers. Chop up the pepper slices, and mix into the cheese stuffing. Stuff each pepper with cheese mixture, and wrap each stuffed pepper in a half bacon slice. Secure with toothpicks.",\
        list_order=3, recipe_id=8
    ),
    Instruction(
        specification="Grill the poppers on a less-hot part of the grill until the peppers are hot and juicy and the bacon is browned, 30 to 40 minutes.",\
        list_order=4, recipe_id=8
    ),
])

    db.session.add.all([
    Instruction(
        specification="Place wakame in a fine-mesh sieve and soak in some cold water for 10 minutes.",\
        list_order=1, recipe_id=9
    ),
    Instruction(
        specification="Combine 4 cups water and dashi granules in a saucepan and bring to a boil over medium heat. Add miso paste and whisk to dissolve. Add wakame and simmer for 3 minutes.",\
        list_order=2, recipe_id=9
    ),
    Instruction(
        specification="Divide tofu between 4 serving bowls. Ladle miso soup on top and garnish with green onions.",\
        list_order=3, recipe_id=9
    ),
])

    db.session.add.all([
    Instruction(
        specification="Place bacon in a large, deep skillet. Cook over medium high heat until evenly brown. Drain, crumble and set aside.",\
        list_order=1, recipe_id=10
    ),
    Instruction(
        specification="Preheat oven to 350 degrees F (175 degrees C). Lightly grease a 9 inch pie pan.",\
        list_order=2, recipe_id=10
    ),
    Instruction(
        specification="Line bottom of pie plate with cheese and crumbled bacon. Combine eggs, butter, onion, salt, flour and milk; whisk together until smooth; pour into pie pan.",\
        list_order=3, recipe_id=10
    ),
    Instruction(
        specification="Bake in preheated oven for 35 minutes, until set. Serve hot or cold.",\
        list_order=4, recipe_id=10
    ),
])

#     db.session.add.all([
#     Instruction(
#         specification="",\
#         list_order=1, recipe_id=
#     ),
#     Instruction(
#         specification="",\
#         list_order=2, recipe_id=
#     ),
#     Instruction(
#         specification="",\
#         list_order=3, recipe_id=
#     ),
# ])



    db.session.add(crab_cheddar_quiche_1)
    db.session.add(crab_cheddar_quiche_2)
    db.session.add(crab_cheddar_quiche_3)
    db.session.add(crab_cheddar_quiche_4)
    db.session.add(autumn_cheescake_1)
    db.session.add(autumn_cheescake_2)
    db.session.add(autumn_cheescake_3)
    db.session.add(autumn_cheescake_4)


    db.session.commit()


def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()
