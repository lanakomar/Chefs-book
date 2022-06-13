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

    db.session.add_all([
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

    db.session.add_all([
        Instruction(
            specification="Place the watermelon pieces onto a plastic-wrapped baking sheet, and freeze until solid, about 45 minutes.",\
            list_order=1, recipe_id=4
        ),
        Instruction(
            specification="Place the frozen watermelon, water, and strawberry lemonade drink mix in a blender; blend until slushy.",\
            list_order=2, recipe_id=4
        ),
    ])

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
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

    db.session.add_all([
    Instruction(
        specification="Lay beef strips out in a single layer on a baking sheet lined with paper towels. Allow to dry in the refrigerator for 30 minutes. In a small bowl, mix together the sugar, rice vinegar, orange juice concentrate, salt and soy sauce. Set aside.",\
        list_order=1, recipe_id=11
    ),
    Instruction(
        specification="Meanwhile, combine rice and water in a medium saucepan. Bring to a boil, then reduce heat to medium-low and simmer for 20 minutes, or until rice is tender. Add more water at the end if necessary.",\
        list_order=2, recipe_id=11
    ),
    Instruction(
        specification="Heat oil in a wok over medium-high heat. Toss dried beef in cornstarch to coat. Fry in the hot oil in small batches until crispy and golden brown; set aside. Drain all of the oil from the wok except about 1 tablespoon.",\
        list_order=3, recipe_id=11
    ),
    Instruction(
        specification="Add orange zest, ginger and garlic to the remaining oil, and cook briefly until fragrant. Add the soy sauce mixture to the wok, bring to a boil, and cook until thick and syrupy, about 5 minutes. Add beef, and heat through, stirring to coat. Serve immediately over steamed rice, and garnish with broccoli.",\
        list_order=4, recipe_id=11
    ),
])

    db.session.add_all([
    Instruction(
        specification="Make the crust: Line a 9-inch-by-13-inch baking pan with parchment paper, leaving a 2-inch overhang on 2 sides. In a food processor, or in a resealable plastic bag, crush the graham crackers until you have fine crumbs (but stop before you have dust). You should have about 2 1/4 cups. Transfer the crumbs to a medium bowl. Add the butter, sugar and salt and stir until evenly moistened. Tip the crumbs into the prepared pan and press them down into an even layer on the bottom. Transfer to the freezer while you prepare the filling.",\
        list_order=1, recipe_id=12
    ),
    Instruction(
        specification="Make the filling: Set the chocolate in a medium bowl. In a small saucepan, heat 1 cup cream, espresso powder and salt until hot but not boiling. Pour the hot cream mixture over the chocolate and let it stand for 2 minutes. Add the vanilla and whisk until smooth. Set aside to cool completely.",\
        list_order=2, recipe_id=12
    ),
    Instruction(
        specification="In a large bowl or in the bowl of a stand mixer fitted with the whisk attachment, whip the remaining 2 cups heavy cream until you have stiff peaks. Add the chocolate mixture and gently fold to combine. Pour the mixture over the prepared crust, and spread it out into an even layer. Cover with plastic wrap and chill until firm, at least 2 hours. To serve, cut the two edges without parchment free with a sharp knife then use the parchment overhang to transfer the bar to a cutting board. Cut into squares and serve with a dollop of whipped cream, if desired.",\
        list_order=3, recipe_id=12
    ),
])

    db.session.add_all([
    Instruction(
        specification="In a large bowl combine 3 cups cubed watermelon; 2 large ripe tomatoes, chopped; 1 medium cucumber, peeled, seeded and chopped; 1 small red onion, sliced; 1/3 cup pitted kalamata olives; 1/3 cup crumbled feta; and some chopped parsley and mint. Drizzle with olive oil and red-wine vinegar, sprinkle with salt and pepper, toss and serve.",\
        list_order=1, recipe_id=13
    )
])

    db.session.add_all([
    Instruction(
        specification="Heat your grill to medium-high. Grill corn, turning occasionally, until cooked through and lightly charred, 10 to 12 minutes. (Alternatively, add corn to a large pot of salted boiling water and cook for 5 to 7 minutes.)",\
        list_order=1, recipe_id=14
    ),
    Instruction(
        specification="Meanwhile, in a small bowl, mix together butter, half the lemon zest and 1/4 teaspoon Old Bay seasoning.",\
        list_order=2, recipe_id=14
    ),
    Instruction(
        specification="Slather hot corn with butter mixture. Sprinkle with the remaining zest and Old Bay seasoning, to taste. Serve with lemon wedges alongside for squeezing.",\
        list_order=3, recipe_id=14
    ),
])

    db.session.add_all([
    Instruction(
        specification="Heat oven to 425 degrees. Place bacon in a 9-inch oven-safe skillet, then set over medium heat. Cook, stirring occasionally, until fat has rendered and bacon has browned on the edges, 7 to 10 minutes.",\
        list_order=1, recipe_id=15
    ),
    Instruction(
        specification="Meanwhile, in a large bowl, whisk together flour, salt, pepper and baking powder. In a medium bowl, whisk together eggs and milk, then whisk egg mixture into flour. Stir in Parmesan and half the chives.",\
        list_order=2, recipe_id=15
    ),
    Instruction(
        specification="Once bacon is crisp and brown, raise heat to medium-high, and add butter, stirring until melted. Pour batter into skillet, then quickly arrange Camembert pieces on top.",\
        list_order=3, recipe_id=15
    ),
    Instruction(
        specification="Transfer pan to the oven, and bake until puffed and golden, 20 to 25 minutes. Sprinkle with remaining chives, and serve immediately.",\
        list_order=4, recipe_id=15
    ),
])

#     db.session.add_all([
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
