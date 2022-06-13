from app.models import db, Note, recipe


def seed_notes():
    db.session.add_all([
        Note(content="Another keeper. Modified it a bit by adding mushrooms and green onion. Also, light cream instead of whole milk. Of course, real crab instead of the fake stuff. Easy and simply a good quiche", date_created="2020-11-4", recipe_id=1, author_id=3),\
        Note(content="This came out really good, not too hard or runny. I would maybe cut the parsley back by half.", date_created="2021-08-22", recipe_id=1, author_id=4),\
        Note(content="Used Monterey Jack cheese instead of cheddar and used whole cream instead of milk. Added extra cheese shreds on top. It was divine!", date_created="2022-01-30", recipe_id=1, author_id=2),\
        Note(content="I made this, it was great. I added diced baby portabella mushrooms, 1/2 cup diced green onions. It turned out great my family loved it.", date_created="2022-04-15", recipe_id=1, author_id=1),\

        Note(content="Excellent cheesecake! I made this for Easter and my hubby raved and called it a keeper...it tastes even better the next day...", date_created="2019-04-04", recipe_id=2, author_id=12),\
        Note(content="This cheesecake was really good. I used granny smith apples and doubled the cheese mixture I baked it for about 80 minutes, it turned out really creamy! Wonderful when topped with caramel sauce.", date_created="2019-08-09", recipe_id=2, author_id=12),\
        Note(content="Much has been written about doubling the crust and filling ingredients and pre-cooking the apples - all great tips. Not as much, however, has been said about the wonderful texture and creaminess of this cheesecake. I'm sure the water bath has a lot to do with this, so don't skip this step. The filling is so good I think I'll use it as a standard recipe to use with other add-ins and toppings.", date_created="2020-10-30", recipe_id=2, author_id=5),\
        Note(content="This was a HUGE hit at a cheesecake party. I made the following changes after reading pages of reviews: I doubled the crust mixture, and sprinkled half on the top with 20 minutes left to bake, I doubled the filling, I chopped the apples and then microwaved them until they were soft and drained the liquid before tossing with sugar. It was beautiful and awesome!", date_created="2021-05-05", recipe_id=2, author_id=8),\
        Note(content="I want to give this cheesecake 6 stars. It was wonderful everyone loved it. I had to cook mine for 80 minutes till it was firm. Thank you for this wonderful dessert!!!!!", date_created="2021-06-21", recipe_id=2, author_id=13),\
        Note(content="Is cheesecake a CAKE? I don't know.... But this one turned out to be awesome!", date_created="2021-12-01", recipe_id=2, author_id=7),\

        Note(content="I LOVED IT!! My husband always seasons the steaks and he was not happy when he saw me pouring lemmon pepper all over his precious t bones but they were fabulous. Very juicy due to the beer and so simple to make. I used Shiner Bock beer and I would definately reccoment a dark beer.", date_created="2020-01-20", recipe_id=3, author_id=12),\
        Note(content="This was AWFUL! I used Killians beer and followed the directions. The lemon pepper did not go well with the beer. Yuck!", date_created="2020-07-09", recipe_id=3, author_id=8),\
        Note(content="I was very sSurprised at how good this tastes! I was a bit leary of lemon pepper and beer, but it really works!", date_created="2021-08-20", recipe_id=3, author_id=9),\
        Note(content="I marinated mine too long. We were having grill problems and I left the steak in the marinade close to 3 hours. The steak was dry but had a nice flavor. I will definately try it again and marinate it for about an 1-1 1/2 hours.", date_created="2022-04-13", recipe_id=3, author_id=10),\
        Note(content="I am by no means a cook. I am just starting out, and my fiance and I made this recipe last night and it was fabulous! We used a frying pan as well since we do not own a grill. I am just amazed at myself that I can cook something tasty! ;)", date_created="2022-06-18", recipe_id=3, author_id=11),\

        Note(content="Great after school snack for kiddos....and so much better than a Sonic slushy! I used regular lemonade mix, and they loved it.", date_created="2019-09-09", recipe_id=4, author_id=13),\
        Note(content="I only rated this three stars because it was too bland/simple. I had to add some frozen lime juice, crushed ice and Tequila! Awesome!", date_created="2020-06-24", recipe_id=4, author_id=7),\
        Note(content="Great after school snack for kiddos....and so much better than a Sonic slushy! I used regular lemonade mix, and they loved it.", date_created="2021-09-09", recipe_id=4, author_id=1),\
        Note(content="so good and so easy! Plus, I now know to freeze my surplus melon for use later! I love it!", date_created="2022-06-12", recipe_id=4, author_id=2),\

        Note(content="Watch this closely, the breading browns very quickly. I liked the addition of the Dijon mustard.", date_created="2019-08-05", recipe_id=5, author_id=1),\
        Note(content="Pretty darn good! I used chicken tenders, so the cook-time was even shorter, and everyone liked them! Definitely a do-again!", date_created="2020-02-18", recipe_id=5, author_id=4),\
        Note(content="Only change is that I would pound the chicken first if it's a large breast, and also I would put the chicken on a rack in the baking pan and turn it over halfway through so the bottom gets crispy as well. Very tasty tho and I would definitely make it again!", date_created="2020-09-26", recipe_id=5, author_id=6),\
        Note(content="It was terrific! I made it exactly as the recipe is, I wouldn't change a thing. The chicken was easy to make, tender and had great flavor! I will definitely add it to my chicken recipes. Thanks!", date_created="2021-06-14", recipe_id=5, author_id=8),\
        Note(content="I am HOOKED! We loved it and it WILL be a staple in my house! THANK YOU for this super easy, minimal effort and time saving recipe!", date_created="2021-10-22", recipe_id=5, author_id=10),\
        Note(content="Great tasting and super easy to prepare! Even my four year old daughter licked her plate.", date_created="2022-02-11", recipe_id=5, author_id=12),\
        Note(content="Awesome recipe. I added an egg white to the butter/Dijon mix. The chicken breasts came out moist and tender. Also, the same recipe worked great with thick cut boneless pork chops.", date_created="2022-03-26", recipe_id=5, author_id=3),\

        Note(content="Absolutely wonderful! We didnt have enough pasta for 4 people, so I also made some Spanish rice to go with it. My whole family loved it.", date_created="2019-04-20", recipe_id=6, author_id=7),\
        Note(content="This is quick meal, I liked the concept of it, but , I would use heavy cream next time and add pepper.", date_created="2019-12-31", recipe_id=6, author_id=13),\
        Note(content="Added more garlic , very yummy!", date_created="2020-02-28", recipe_id=6, author_id=5),\
        Note(content="This is so good and so easy! I did liberally sprinkle the shrimp with Old Bay seasoning and let set for 1/2 hr. before cooking. Also added more garlic. Can’t thank you enough for posting this great recipe! It’s a keeper.", date_created="2020-03-09", recipe_id=6, author_id=11),\
        Note(content="Love, love, love! So easy to make. A little rich, but, yeah.... : )", date_created="2021-05-18", recipe_id=6, author_id=3),\
        Note(content="I make this dish often, usually when I'm runny late and need something quick for dinner. I always have pasta in the pantry and shrimp in the freezer. This dish is a snap to make.", date_created="2021-11-10", recipe_id=6, author_id=9),\
        Note(content="This was creamy and delicious! I used heavy cream instead of half and half and a pinch of oregano instead of parsley which I did not have.", date_created="2022-02-20", recipe_id=6, author_id=1),\

        Note(content="I really enjoyed this recipe. However, I took the very thick tuna steaks pretty much directly from the fridge to the skillet and they were (obviously) still cold in the middle during consumption. Next time, I'll let the tuna come closer to room temperature before searing.", date_created="2019-06-27", recipe_id=7, author_id=4),\
        Note(content="simple and delicious. Ran into a friend who is a chef when I was buying the wine the recipe called for and he said to forget it, it won't matter. He was right!", date_created="2019-11-08", recipe_id=7, author_id=7),\
        Note(content="This recipe is unbelievably easy and fantastic. I used brown sugar because I didn't have honey (allergic) and I doubled the dipping sauce. Half the sauce I used to marinate the tuna steaks for about 2 hours, and the rest for dipping. I have never had a recipe disappear so fast. Definitely my new favorite fish recipe.", date_created="2020-01-16", recipe_id=7, author_id=9),\
        Note(content="Delicious. I have been waiting to try this recipe for a while now. I only make fresh tuna for occasions and it was sensational. The sesame seeds were a great crunchy contrast to the tuna steaks. Seared them for only 30 seconds on each side. Hubby loved this...and I did too. (So did my 1 1/2 year old son who doesn't like fresh tuna). Will be used again and again.", date_created="2020-10-07", recipe_id=7, author_id=12),\
        Note(content="I have been looking for a recipe like this one!! The flavor and texture of the tuna was awesome. I did not have the mirin wine. Used a little white wine and still was great! Sesame seeds to scorch easily. I was dancing around when we were eating it as an appetizer. Also made some wasabi vinegrette and served it with the soy sauce as well!! Thanks!", date_created="2021-02-01", recipe_id=7, author_id=1),\
        Note(content="Excellent recipe. I made this for dinner tonight and it was a hit. The only change I made was I substituted Agave nectar for the honey because my husband is diabetic. Served with a rice salad of jasmine rice, julienned carrots, peas, diced red onions and thinly sliced jalepenos. I will make this again.", date_created="2021-08-09", recipe_id=7, author_id=3),\

        Note(content="These are great. But SUPER HOT! I also cheated and cooked them in the oven. Turned out great. I also added garlic and onion powder to the cheese mixture.", date_created="2019-03-05", recipe_id=8, author_id=10),\
        Note(content="I took this three *recipe to a 5 * by adding my own touch! doubled the parmasan,instead of chopping the tops I put them back on to help hold the cheese in,and precook the bacon about half way before wrapping,the bacon will still be pliable but will crisp up nicely on the grille!!", date_created="2019-09-09", recipe_id=8, author_id=13),\
        Note(content="These were gone in a flash. My husband made me make them again the next day and I have to make them for his work this week. Easy and delicious:) I cut the jalapenos in half b/c my husband wanted more bacon per bite ratio. :) You also don't need a toothpick.", date_created="2020-03-28", recipe_id=8, author_id=9),\
        Note(content="I made these at a tailgate, and everyone raved about them. They were the perfect way to use up the remaining jalepenos from my garden before the weather got too cold.", date_created="2020-12-15", recipe_id=8, author_id=8),\
        Note(content="These turned out great. I wore gloves when working with the jalapenos and didn't have any problems.", date_created="2021-09-21", recipe_id=8, author_id=5),\
        Note(content="TRY MAKEING A BURGER WITH A ITEM I FOUND ON THE NET CALLED BURGER POCKET PRESS, AND USE THESE ING. EXCEPT THE CREAM CHEESE CROPPED UP BACON AND ADD THE REST OF THE ING. ALWSOME", date_created="2022-02-09", recipe_id=8, author_id=2),\

        Note(content="I suggest using firm tofu (it is easier to handle) and letting it drain first. Cut it in half and let it sit on some paper towels for a bit before you use it. This allows the tofu to better absorb the flavor of the broth.", date_created="2019-04-07", recipe_id=9, author_id=4),\
        Note(content="This was a big hit! I could not find dashi anywhere, so substituted fish bouillon. I added fresh spinach and prawns before the tofu to make it a meal.", date_created="2019-07-14", recipe_id=9, author_id=2),\
        Note(content="This had a nice taste but the silken tofu I used was too soft. I suggest a firm tofu. I also used a dashi that was MSG free. I think that is why it needed some salt for me. A really easy and quick recipe.", date_created="2020-09-30", recipe_id=9, author_id=8),\
        Note(content="this is a great soup! we love japanese food but found most of the recipes are hard to follow. this is simple and taste just like the one you get in the restaurant. thanks.", date_created="2021-02-02", recipe_id=9, author_id=10),\
        Note(content="Tastes identical to miso soup you would buy at a restaurant. The measurements are just right! We love miso soup, but I have had a hard time getting the ingredients until now!", date_created="2021-08-19", recipe_id=9, author_id=12),\
        Note(content="Great recipe! I make this soup all the time. My only addition to it would be one sheet of nori (dried seaweed) cut into pieces gives it a great flavor. You also can add one beaten raw egg to make it an egg drop soup!", date_created="2022-01-25", recipe_id=9, author_id=1),\

        Note(content="I have made this quiche many times. My recipe calls for a 1/2 cup of complete pancake mix instead of flour. Quick and very good!", date_created="2019-09-17", recipe_id=10, author_id=4),\
        Note(content="OH MY GOD! This quiche is amazing! I used Colby/Jack Cheese cause I didn't have any swiss and I cut the milk by 1/4 of a cup and it was perfect! Nice and crispy with a great bacony flavor! Three cheers for quick quiche!", date_created="2020-08-04", recipe_id=10, author_id=6),\
        Note(content="This is the first recipe from this site that I had very low expections, and I was wrong!! This was wonderful! My changes: Omitted bacon, added broccoli and mushrooms, sprinkled paprika on top to add to the 'browned' look, which it did beautifully. I love this recipe!", date_created="2021-01-12", recipe_id=10, author_id=8),\
        Note(content="It's a keeper! I used some of the reviews and cooked the onions about 2 min before adding to egg mixture. Blender is the way to mix this one. Also baked in my cast iron skillet 35 min it turned out beautiful. No need to broil.", date_created="2021-08-16", recipe_id=10, author_id=10),\
        Note(content="I made this tonight, all the family loved it. Simple, filling and perfect.", date_created="2022-02-27", recipe_id=10, author_id=12),\

        Note(content="Sauce is what makes it great. Like others, we altered it by: using 1/3 cup orange juice instead of concentrate *and* stirfrying batches with only 1 Tbs of peanut oil each time. Cuts down on calories and left the meat tender and glossy. Pretty authentic tasting.", date_created="2019-04-07", recipe_id=11, author_id=2),\
        Note(content="Turned out fantastic. I did as others suggested and doubled the sauce while cutting the sugar in half. I also omitted the orange peel as it really didn't need it. Next time I will reduce the vinegar by 25% and use mixed OJ to replace the 25% vinegar omission. Really very good. I will make again.", date_created="2019-10-12", recipe_id=11, author_id=1),\
        Note(content="I added only 1 TBS of ginger, and this was delicous! My husband enjoyed it too. As other's have noted, cutting back on the ginger keeps it from overpowering the meat. I can't wait to make this again!", date_created="2020-07-25", recipe_id=11, author_id=5),\
        Note(content="this was SOOOOO yummy but the sauce as is is way too sweet, so I ended up doubling everything in the sauce except the sugar. I only had about a pound of beef and I only had white vinegar, I did add some sriachi to the sauce for a little kick", date_created="2020-11-16", recipe_id=11, author_id=8),\
        Note(content="awesome! I just sauteed the beef in a little olive oil instead of deep frying and it still was very good.", date_created="2021-03-29", recipe_id=11, author_id=3),\
        Note(content="This was terrific! I used flank steak that I bought to make something else, so it took a while to cut it all up, but well worth the time. It looked authentic, and my half chinese roommate liked it too!", date_created="2022-02-26", recipe_id=11, author_id=10),\

        Note(content="Are the bars messy to eat by hand? Or do you need a plate and fork?", date_created="2019-05-20", recipe_id=12, author_id=1),\
        Note(content="Instead of cream, use two eggs beaten for five minutes each, added one at a time. It’s the French Silk Mocha Pie recipe I’ve been making for 45 years. A family favorite!", date_created="2019-08-02", recipe_id=12, author_id=12),\
        Note(content="The best dessert I’ve had in a long time! This was absolutely amazing for two reasons: the rush sweet chocolate taste and the light creamy consistency—a seriously dangerous and addictive combination.", date_created="2020-10-30", recipe_id=12, author_id=6),\
        Note(content="Use nut meal (or grinding toasted nuts in a food processor) to replace graham cracker crumbs", date_created="2021-07-15", recipe_id=12, author_id=4),\
        Note(content="These are easy and delicious! I took them to a party and got rave reviews and some guests took a few home with them. I used half Nestle’s toll house standard chocolate chips and half Giardelli bittersweet. I will make these again and again. Would also make a mouth watering chocolate pie!", date_created="2022-04-18", recipe_id=12, author_id=7),\

        Note(content="Best. Summer. Salad. Period. Make sure to use well chilled watermelon straight from the fridge. Also, I used white balsamic vinegar (condimento bianco) which worked wonderfully.", date_created="2019-06-30", recipe_id=13, author_id=4),\
        Note(content="This was really good. I don't love raw onions, so I quick pickled the onions a few hours ahead in a red wine vinegar/olive oil mix and used that as the dressing.", date_created="2019-08-07", recipe_id=13, author_id=6),\
        Note(content="Thanks for a good idea for a summer salad. Please stop excluding vegetable and fruit prep time from the recipe Time. It’s very misleading. I see this in most recipes on this site and elsewhere. Cubing the watermelon could double the time if not more.", date_created="2020-05-04", recipe_id=13, author_id=8),\
        Note(content="I'm with you on the raw onion thing! One solution is to soak them in ice water for a bit then rinse. It really mellows them!", date_created="2020-09-07", recipe_id=13, author_id=10),\
        Note(content="I used Casteveltrano olives and plain goat cheese, no herbs and Sherry vinegar. Simple, clean and delicious; everyone likes it!", date_created="2021-06-03", recipe_id=13, author_id=12),\
        Note(content="I prefer it on a bed of arugula, olives optional.", date_created="2022-03-30", recipe_id=13, author_id=1),\

        Note(content="You can also put the Old Bay on, wrap in foil and grill. Gives the corn an 'almost sweet' taste. Either way - it's Yumbo!", date_created="2020-07-07", recipe_id=14, author_id=3),\
        Note(content="Replaced the butter with vegan Mayo and added some miso worked beautifully with the lemon and old bay seasoning", date_created="2021-06-28", recipe_id=14, author_id=1),\
        Note(content="I always grill corn on the cob with the husk on. It steams the corn nicely and you can still put some char on it after shucking.", date_created="2021-08-19", recipe_id=14, author_id=5),\
        Note(content="The Old Bay compound butter is a revelation, definitely a future barbecue mainstay.", date_created="2022-05-14", recipe_id=14, author_id=7),\

        Note(content="If you pour the batter into the hot pan in a spiral pattern, it will be easier to serve. Pouring the batter in one spot cools the pan and makes the pancake stick to the metal.", date_created="2020-06-12", recipe_id=15, author_id=13),\
        Note(content="For a vegetarian variant, I threw two teaspoons of smoked paprika and a tsp of powdered shallots into the oil and cooked it for a minute before mixing in the batter. It worked well.", date_created="2020-11-06", recipe_id=15, author_id=11),\
        Note(content="Yum! Second time I added some sauteed apples under the cheese...just to try bumping it up since apples and camembert go so well together. Home run!", date_created="2020-12-23", recipe_id=15, author_id=9),\
        Note(content="Serve with fig jam ... yum!", date_created="2021-03-09", recipe_id=15, author_id=7),\
        Note(content="This was wonderful. Couldn't find camembert so used brie. Also used probably a bit more than half of the wheel, the whole wheel seemed a bit much. Great warmed up the next day, too. Yum", date_created="2021-12-30", recipe_id=15, author_id=1),\
        Note(content="Too greasy and weak flavor. Drain ALL the bacon grease off and decrease the butter. I agree with those who would add onions and use cheddar.", date_created="2022-02-04", recipe_id=15, author_id=3),\

        # Note(content="", date_created="2020-10-30", recipe_id=, author_id=5),\
    ])

    db.session.commit()


def undo_notes():
    db.session.execute('TRUNCATE notes RESTART IDENTITY CASCADE;')
    db.session.commit()
