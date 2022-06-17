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

    db.session.add_all([
    Instruction(
        specification="Make the meat filling: Place the chopped onion in a food processor and process until it is very fine and has started to release moisture. Transfer the onion to a large bowl. Add the beef, pork, black pepper and salt, and mix very well. Gradually add kefir to the mixture and mix it into the meat using a spoon. The consistency should be pourable and almost soupy, not stiff. If necessary, add more kefir, 1 tablespoon at a time, to achieve the desired consistency. Cover mixture and place it in the refrigerator to chill for 1 hour.",\
        list_order=1, recipe_id=16
    ),
    Instruction(
        specification="Make the dough: Place 3 cups of the flour in a large bowl. Add the fine salt and mix with a fork. Add the water and mix until combined. Sprinkle a work surface with some of the remaining flour and knead in the rest of the flour little by little (you may not need all of it), until the dough is pliable and not sticky, about 15 minutes. (The dough should spring back when you make a slight indent with your finger.) Shape the dough into a ball, place in a bowl, cover tightly with plastic wrap and let rest for at least 1 hour.",\
        list_order=2, recipe_id=16
    ),
    Instruction(
        specification="Set up your frying station: Pour 2 inches of oil into a wok or a Dutch oven. Line a sheet pan with a wire rack and some paper towels to absorb any excess oil from the finished chebureki. Heat the oil over medium-high until the temperature reaches between 350 and 375 degrees.",\
        list_order=3, recipe_id=16
    ),
    Instruction(
        specification="Divide the rested dough into 12 pieces and roll them into balls. (The dough should be pliable and shouldn’t need much flour.) Flatten the pieces into disks and cover with plastic wrap so they don’t dry out. Working with one piece at a time, lightly dust the counter with flour and roll out the dough into a very thin round about 8 inches in diameter. (You should be able to read text through the dough.)",\
        list_order=4, recipe_id=16
    ),
    Instruction(
        specification="Place 3 level tablespoons of filling on one side of the round and spread it into a thin half-moon, leaving a 1-inch border around the filling. Make sure not to add too much filling! Overfilling increases the risk of leakage during frying.",\
        list_order=5, recipe_id=16
    ),
    Instruction(
        specification="Fill a small bowl with water, and using your finger, dampen the edges of the whole round to help seal the cheburek. Fold the dough over the side with the filling, trying to make sure there are no air bubbles between the filling and the dough to help decrease the chance of bursting. Press the edges to seal tightly, then seal them completely with a fork. Use a pasta wheel or paring knife to trim off any uneven edges, if you like.",\
        list_order=6, recipe_id=16
    ),
    Instruction(
        specification="Once the oil is at 350 degrees, carefully lower the shaped cheburek into the oil and fry until the dough is golden brown and bubbly, about 2 minutes per side. Using tongs or a large slotted spatula, transfer the fried cheburek to the rack. Repeat shaping, filling and frying with the remaining dough and filling.",\
        list_order=7, recipe_id=16
    ),
    Instruction(
        specification="Let the cheburek cool slightly, then dig in! These are best eaten hot. Enjoy with a glass of ryazhanka or kefir.",\
        list_order=8, recipe_id=16
    ),
])

    db.session.add_all([
    Instruction(
        specification="Lay pork chops on a baking sheet, and season well on both sides with salt and pepper.",\
        list_order=1, recipe_id=17
    ),
    Instruction(
        specification="Combine eggs and milk in a low, flat bowl. Season with salt, pepper and the small pinch of cayenne.",\
        list_order=2, recipe_id=17
    ),
    Instruction(
        specification="Sprinkle flour generously over the chops on both sides, then shake off excess.",\
        list_order=3, recipe_id=17
    ),
    Instruction(
        specification="Submerge the floured chops in the egg mixture, and turn them over several times to coat well. Leave chops in egg mixture for 5 minutes.",\
        list_order=4, recipe_id=17
    ),
    Instruction(
        specification="Use your left hand to remove a chop from the batter and drain off excess liquid. Place chop on a baking sheet and, with your right hand, heavily sprinkle with bread crumbs on both sides. Repeat with remaining chops.",\
        list_order=5, recipe_id=17
    ),
    Instruction(
        specification="Sprinkle each chop again with crumbs, patting with your hand to make sure crumbs adhere and coat well. Refrigerate, uncovered, until ready to fry.",\
        list_order=6, recipe_id=17
    ),
    Instruction(
        specification="Set a wide cast-iron or other heavy skillet over medium-high heat. Add clarified butter to a depth of 1/2 inch. When butter is hot, lay in the chops without crowding, and let them fry very gently, about 4 to 5 minutes per side, until beautifully golden brown. (Turn down heat if they seem to be browning too fast.) If your pan is small, cook in 2 batches and keep finished chops warm in a 250-degree oven.",\
        list_order=7, recipe_id=17
    ),
    Instruction(
        specification="Blot cooked chops on paper towels. Transfer to a warm platter or individual plates. Serve with lemon wedges.",\
        list_order=8, recipe_id=17
    ),
])

    db.session.add_all([
    Instruction(
        specification="Whisk egg and yolk together in a medium bowl. Add baking powder, sugar and salt; whisk until smooth and fluffy. Pour in half the milk, then half the flour. Using a wooden spoon, stir to combine. Add the remaining milk and flour plus 2 tablespoons clarified butter and stir briefly just until batter comes together but is still somewhat lumpy.",\
        list_order=1, recipe_id=18
    ),
    Instruction(
        specification="Heat a large 12-inch cast-iron skillet or griddle over medium-high for at least 5 minutes. Pour about 1/4 cup clarified butter into the pan. When the surface of the clarified butter starts to shimmer, ladle about 1/3 cup of the batter into the skillet for each pancake, leaving a couple of inches between each pancake. Add more clarified butter as pancakes cook to keep about 1/8 inch of fat in the bottom of the pan at all times.",\
        list_order=2, recipe_id=18
    ),
    Instruction(
        specification="Cook until the top of the pancake starts to bubble and edges turn browned and crisp, 2 to 3 minutes. Use a spatula to flip each pancake. The cooked surface should be very crispy, with a dark ring around the edge. Cook until the second side is browned and crisp, 2 to 3 minutes. Repeat to cook the remaining pancakes, adding more clarified butter as needed.",\
        list_order=3, recipe_id=18
    ),
    Instruction(
        specification="Serve immediately with pats of salted butter, if desired, and maple syrup. If making a large batch, cooked pancakes can be kept warm on a wire rack set in a rimmed metal baking sheet in a 300-degree oven.",\
        list_order=4, recipe_id=18
    ),
])

    db.session.add_all([
    Instruction(
        specification="Heat oven to 375. Bring a large pot of salted water to boil. Add zucchini and blanch for 1 minute. Drain and spread zucchini out to cool on a towel. Season lightly with salt and pepper.",\
        list_order=1, recipe_id=19
    ),
    Instruction(
        specification="Beat eggs and milk with 1/2 teaspoon salt, then add nutmeg, thyme and basil leaves.",\
        list_order=2, recipe_id=19
    ),
    Instruction(
        specification="Butter a 2-quart low-sided baking dish, and arrange blanched zucchini over bottom. Scatter cheese over zucchini, then pour in custard.",\
        list_order=3, recipe_id=19
    ),
    Instruction(
        specification="Bake for 30 minutes or until custard is still a bit jiggly, but an inserted knife comes out clean. Cool to room temperature before serving.",\
        list_order=4, recipe_id=19
    ),
])

    db.session.add_all([
    Instruction(
        specification="Preheat the Oven to 225˚F. Line a large baking sheet with parchment paper. Using your stand mixer, beat 6 egg whites on high speed 1 min until soft peaks form. With the mixer on, gradually add 1 1/2 cups sugar and beat 10 min on high speed, or until stiff peaks form. It will be smooth and glossy.",\
        list_order=1, recipe_id=20
    ),
    Instruction(
        specification="Use a spatula to quickly fold in 1/2 Tbsp lemon juice and 1/2 Tbsp vanilla extract, then fold in 2 tsp corn starch and mix until well blended.",\
        list_order=2, recipe_id=20
    ),
    Instruction(
        specification="Pipe meringue into 3 to 3 1/2 inches wide nests onto the parchment paper using a Wilton 1M Tip. Indent the center with a spoon to allow room for cream. Bake at 225˚ for 1 hr and 15 min then turn the oven off and without opening the door, let meringue in the hot oven another 30 min. Outsides will be dry and crisp to the tap and very pale cream-colored and insides will still be marshmallow soft.",\
        list_order=3, recipe_id=20
    ),
    Instruction(
        specification="Transfer the pavlova with the parchment paper onto the counter or a cookie rack and allow it to cool to room temp. Once cool, you can top them with whipped cream and fruit or store in an airtight container for 3-5 days at room temperature (in a low humidity place).",\
        list_order=4, recipe_id=20
    ),
    Instruction(
        specification="Beat cold whipping cream with 2 Tbsp sugar in the cold bowl for 2 to 2 1/2 minutes or until whipped and spreadable.",\
        list_order=5, recipe_id=20
    ),
    Instruction(
        specification="Pipe frosting onto the pavlova and top with fresh fruit.",\
        list_order=6, recipe_id=20
    ),
])

    db.session.add_all([
    Instruction(
        specification="Prepare the chicken: In a medium bowl, combine jerk seasoning, 1 tablespoon olive oil, garlic powder and smoked paprika. Add chicken and toss to coat. Cover bowl with plastic wrap and let sit in the refrigerator for 2 hours or up to 24 hours. Pull chicken out about 1 hour before cooking, so it comes to room temperature.",\
        list_order=1, recipe_id=21
    ),
    Instruction(
        specification="Heat oven to 400 degrees. Heat the remaining 1 tablespoon olive oil in a cast-iron skillet over medium. Add the chicken to the skillet, and sear chicken on both sides until browned, about 3 minutes per side.",\
        list_order=2, recipe_id=21
    ),
    Instruction(
        specification="Once chicken is seared, transfer the skillet to the oven and roast chicken until internal temperature reaches 165 degrees, 15 to 20 minutes. Transfer to a cutting board, let rest for about 10 minutes, and slice on a bias.",\
        list_order=3, recipe_id=21
    ),
    Instruction(
        specification="As chicken roasts, prepare the pasta: Set a pot of well-salted water to a boil over high heat. Add the pasta, and cook according to the package instructions. Drain and set aside.",\
        list_order=4, recipe_id=21
    ),
    Instruction(
        specification="Add 2 tablespoons oil to a heavy pot set over medium, and sauté bell peppers with green onions until peppers are barely softened, about 4 minutes. Add the minced garlic and cook until it’s fragrant, about another minute.",\
        list_order=5, recipe_id=21
    ),
    Instruction(
        specification="Add the 1/4 cup jerk seasoning to the pot and combine. Add the thyme and pierced pepper. Add heavy cream and vegetable stock and bring to a simmer. Mix in the Parmesan, then add pasta.",\
        list_order=6, recipe_id=21
    ),
    Instruction(
        specification="Top with the jerk chicken, and garnish with green onions. Serve hot.",\
        list_order=7, recipe_id=21
    ),
])

    db.session.add_all([
    Instruction(
        specification="Combine lemon zest, paprika, garlic, 3/4 teaspoon salt and 3/4 teaspoon pepper in a medium bowl. Add shrimp and toss to coat.",\
        list_order=1, recipe_id=22
    ),
    Instruction(
        specification="In a large pot, melt butter over medium-high heat. When butter is foaming, add shrimp and cook, stirring occasionally, until pink and starting to curl, 2 to 3 minutes. Using a slotted spoon, transfer shrimp to a plate; set aside.",\
        list_order=2, recipe_id=22
    ),
    Instruction(
        specification="Add leeks, season with salt and pepper, and cook over medium until leeks are soft and starting to brown on the edges, 4 to 5 minutes, stirring occasionally. Add beans and chicken broth and bring to a boil over high. Lower heat and simmer, 8 to 10 minutes. Stir in reserved shrimp and any juices from the plate, parsley and lemon juice, and season with salt and pepper. Serve with toasted bread.",\
        list_order=3, recipe_id=22
    ),
])

    db.session.add_all([
    Instruction(
        specification="Heat the oven to 325 degrees. With an electric mixer, beat the egg yolks on high speed until thick and light in color. Add the condensed milk and mix on low speed. Still on low speed, add half the lime juice, cream of tartar and then the remaining lime juice, mixing after each addition. Mix well until blended.",\
        list_order=1, recipe_id=23
    ),
    Instruction(
        specification="Pour into pie crust and bake for 10 to 15 minutes, or until the center is firm and dry to the touch. Freeze for at least 3 hours. Serve with whipped cream.",\
        list_order=2, recipe_id=23
    )
])

    db.session.add_all([
    Instruction(
        specification="Place the Anaheim chile on a small baking sheet covered with aluminum foil. Roast it under the broiler, flipping a couple times, until the chile is wilted and its skin is completely charred and wrinkly, 9 to 12 minutes. (Alternatively, you can char the chile directly on a hot comal or a cast-iron pan set over medium heat, or on a grill set to high.)",\
        list_order=1, recipe_id=24
    ),
    Instruction(
        specification="Place the charred Anaheim chile in a plastic bag and close it well. Let it steam and sweat for 5 to 10 minutes.",\
        list_order=2, recipe_id=24
    ),
    Instruction(
        specification="As the Anaheim chile steams, add the serrano chile, onion, cilantro and salt in a bowl or molcajete, and mash until combined. Add the avocado and continue to mix and mash until you form a chunky purée.",\
        list_order=3, recipe_id=24
    ),
    Instruction(
        specification="Once it is cool enough to handle, remove the Anaheim chile from the bag, slip off the charred skin, make a slit down the side and remove the seeds and stem. You could rinse the chile under a thin stream of water, to help remove the seeds, or rinse it off by dipping it into a bowl of water.",\
        list_order=4, recipe_id=24
    ),
    Instruction(
        specification="Finely chop the Anaheim chile. Add it to the avocado mixture, and stir to combine. Season to taste with salt.",\
        list_order=5, recipe_id=24
    ),
])

    db.session.add_all([
    Instruction(
        specification="In a small bowl, combine saffron with 1 tablespoon water and let soak 10 minutes. Place in food processor with yogurt and garlic and purée until smooth and yellow. Place chicken in glass or ceramic bowl; pour yogurt mixture on top, turn to coat; cover and refrigerate at least 3 hours or overnight.",\
        list_order=1, recipe_id=26
    ),
    Instruction(
        specification="In a medium bowl, combine flour, paprika, mint, salt and pepper. Heat a generous half-inch oil in a deep skillet over medium heat. Drop in a bit of bread to test temperature; oil should bubble vigorously. Working in batches to avoid crowding, dredge chicken pieces in flour mixture, then fry until golden brown on both sides, about 5 minutes a side. Remove and drain on paper towels.",\
        list_order=2, recipe_id=26
    ),
    Instruction(
        specification="Sprinkle with salt and serve immediately, topped with walnuts and lemon wedges.",\
        list_order=3, recipe_id=26
    ),
])

    db.session.add_all([
    Instruction(
        specification="Wash, core and slice tomatoes 1/2-inch thick. Arrange slices on a platter or in a shallow wide bowl.",\
        list_order=1, recipe_id=27
    ),
    Instruction(
        specification="Scatter onion and pepper slices over tomatoes and season everything with sea salt. Let sit 10 minutes to draw out juices.",\
        list_order=2, recipe_id=27
    ),
    Instruction(
        specification="Break feta into rough chunks and scatter over salad. Sprinkle mint and oregano over top, drizzle generously with olive oil and serve.",\
        list_order=3, recipe_id=27
    ),
])

    db.session.add_all([
    Instruction(
        specification="Slice the steak first with the grain into 2-inch wide strips. Then cut each strip across the grain into 1/4-inch thick slices. Place in a medium bowl and toss with the cornstarch, 1 teaspoon of the rice wine or sherry, the soy sauce, one of the minced garlic cloves, salt and pepper to taste, 1 teaspoon cold water, and the sesame oil.",\
        list_order=1, recipe_id=28
    ),
    Instruction(
        specification="Combine the remaining rice wine or sherry and the hoisin sauce in a small bowl and set aside.",\
        list_order=2, recipe_id=28
    ),
    Instruction(
        specification="Heat a 14-inch flat-bottomed wok over high heat until a drop of water evaporates within a second or two when added to the pan. Swirl in 1 tablespoon of the oil and add the beef in a single layer. Let sit in the pan for about 1 minute, until it begins to sear, then stir fry for 1 minute. Transfer to a plate or bowl.",\
        list_order=3, recipe_id=28
    ),
    Instruction(
        specification="Swirl in the remaining oil, then add the garlic, ginger and red pepper flakes and stir-fry for no more than 10 seconds. Add the mushrooms and peppers, sprinkle with salt to taste and stir-fry for 1 to 2 minutes. Return the beef and any juices that have accumulated on the plate or bowl to the wok, add the hoisin sauce mixture and stir-fry for another 30 seconds to a minute, until the beef is cooked through. Remove from the heat and serve with rice, grains or noodles.",\
        list_order=4, recipe_id=28
    ),
])

    db.session.add_all([
    Instruction(
        specification="Heat oven to 375 degrees and position an oven rack in upper third of oven. Use 1 tablespoon butter to grease a 9-inch round or square baking pan.",\
        list_order=1, recipe_id=29
    ),
    Instruction(
        specification="In a blender, purée cottage cheese, milk, mustard, cayenne, nutmeg and salt and pepper. Reserve 1/4 cup grated Cheddar for topping. In a large bowl, combine remaining grated Cheddar, milk mixture and uncooked pasta. Pour into prepared pan, cover tightly with foil and bake 30 minutes.",\
        list_order=2, recipe_id=29
    ),
    Instruction(
        specification="Uncover pan, stir gently, sprinkle with reserved cheese and dot with remaining tablespoon butter. Bake, uncovered, 30 minutes more, until browned. Let cool at least 15 minutes before serving.",\
        list_order=3, recipe_id=29
    ),
])

    db.session.add_all([
    Instruction(
        specification="Heat oven to 425 degrees and butter a 10-ounce ramekin. Dust the buttered ramekin with granulated sugar.",\
        list_order=1, recipe_id=30
    ),
    Instruction(
        specification="Combine the chocolate and 3 tablespoons butter in a heat-safe bowl set over a pan of simmering water. Cook, stirring occasionally, until melted and smooth. (Alternatively, combine in a bowl and microwave in 30-second blasts, stirring in between, until melted and smooth, about 1 minute.) Remove from the heat and set aside.",\
        list_order=2, recipe_id=30
    ),
    Instruction(
        specification="In a medium bowl, combine the 3 tablespoons sugar, egg, egg yolk, vanilla and salt. Whisk vigorously until the mixture is thick, foamy and pale, about 2 minutes. Whisk in the flour until smooth.",\
        list_order=3, recipe_id=30
    ),
    Instruction(
        specification="Using a spatula, add the chocolate to the egg mixture and stir gently until combined.",\
        list_order=4, recipe_id=30
    ),
    Instruction(
        specification="Pour the mixture into the ramekin. Bake for 12 to 14 minutes or until the edges are set and puffed, but the center is still soft when lightly pressed. (You can also cover and refrigerate the batter up to a day in advance. Add an additional minute or 2 to baking time if you are baking the cake directly from the refrigerator.)",\
        list_order=5, recipe_id=30
    ),
    Instruction(
        specification="Use an offset spatula or small knife to loosen the edges of the cake from the ramekin. Place a plate over the ramekin and carefully invert the warm cake. Use an oven mitt or clean kitchen towel to remove the ramekin, dust the cake with confectioners’ sugar and serve with ice cream or whipped cream.",\
        list_order=6, recipe_id=30
    ),
])


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
