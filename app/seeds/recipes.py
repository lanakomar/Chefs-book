from app.models import db, Recipe


def seed_recipes():
    crab_cheddar_quiche = Recipe(
        title="Crab and Cheddar Quiche",
        time_to_cook="55 mins",
        description="Easy crab quiche. Great for any meal or occasion.",
        servings=8,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image1.jpeg",
        user_id=1
    )

    autumn_cheesecake = Recipe(
        title="Autumn Cheesecake",
        time_to_cook="4 hours",
        description="This is a delicious Apple Cheesecake that I usually make in the fall.",
        servings=12,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image2.jpeg",
        user_id=2
    )

    beer_steak = Recipe(
        title="Beer steak",
        time_to_cook="2 hrs 20 mins",
        description="Grilled steak with a simple beer marinade!",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image3.jpeg",
        user_id=3
    )

    watermelon_lemonade = Recipe(
        title="Refreshing Watermelon Lemonade Slush",
        time_to_cook="50 mins",
        description="Whenever I have excess seasonal fruit, I freeze it in chunks for fast and easy slushes and smoothies. Here's a delicious way to use up some watermelon.",
        servings=2,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image4.webp",
        user_id=4
    )

    parmesan_chicken = Recipe(
        title="Quick Crispy Parmesan Chicken Breasts",
        time_to_cook="50 mins",
        description="These are delicious, easy, quick, and so versatile! Eat them plain, topped with your favorite spaghetti sauce, or sliced on a Caesar salad.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image5.jpeg",
        user_id=5
    )

    creamy_shrimp = Recipe(
        title="Creamy Shrimp Scampi with Half-and-Half",
        time_to_cook="20 mins",
        description="Dinner doesn't have to take forever--prove it with this fast and delicious shrimp scampi recipe.",
        servings=2,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image6.jpeg",
        user_id=6
    )

    seared_tuna = Recipe(
        title="Sesame-Seared Tuna",
        time_to_cook="11 mins",
        description="This sesame-seared tuna is an easy, great-tasting dish. Fresh tuna steaks are coated with sesame seeds, then quickly seared and served rare, so be sure to use good quality fresh tuna.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image7.jpeg",
        user_id=7
    )


    grilled_jalapeno = Recipe(
        title="Grilled Jalapeno Poppers",
        time_to_cook="30 mins",
        description="Best poppers you'll have off your grill! Any left over cheese mixture makes a good spread for crackers while you're waiting.",
        servings=16,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image8.jpeg",
        user_id=8
    )


    miso_soup = Recipe(
        title="Homemade Miso Soup",
        time_to_cook="30 mins",
        description="Make your very own Japanese miso soup from scratch. It's easy to do at home! Perfect for an appetizer or light, warming lunch.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image9.jpeg",
        user_id=9
    )

    quick_qiuiche = Recipe(
        title="Quick Quiche",
        time_to_cook="50 mins",
        description="When you don't have the time to make a pastry crust, try this quick lunch idea. You may add any other goodies you like, such as ham, chicken, crab, shrimp or broccoli.",
        servings=6,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image10.jpeg",
        user_id=10
    )

    orange_beef = Recipe(
        title="Crispy Orange Beef",
        time_to_cook="1 hrs 5 mins",
        description="A delicious crispy and sweet, yet mildly spiced beef stir-fry recipe. Great served with steamed rice and broccoli.",
        servings=6,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image11.jpeg",
        user_id=11
    )

    mousse_bars = Recipe(
        title="No-Bake Chocolate Mousse Bars",
        time_to_cook="30 mins",
        description="Ethereal and ready to melt in your mouth, chocolate mousse bars are easy to make and even easier to eat. With so few ingredients, it’s important to use a chocolate you would be perfectly happy to snack out of hand. The instant espresso powder is optional but adds depth to this simple dessert. To cut beautiful, neat slices, use a long sharp knife warmed in hot water and wiped clean before each cut.",
        servings=24,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image12.jpeg",
        user_id=12
    )

    watermelon_salad = Recipe(
        title="Greek-Style Watermelon Salad",
        time_to_cook="5 mins",
        description="It's not an immediately obvious combination – watermelon, cucumber, olives and feta – but one bite will leave you convinced that this savory-sweet summer salad is something truly special. The astringent punch of the olives and feta provides a sophisticated counterpoint to the watery mellowness of the melon and cucumber. With a hunk of bread, it's a lovely light lunch; with practically any grilled meat or fish, it's an ideal summer supper.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image13.jpeg",
        user_id=13
    )

    corn = Recipe(
        title="Corn on the Cob With Old Bay and Lemon",
        time_to_cook="15 mins",
        description="If you’ve had the pleasure of eating your way through a bucket of Maryland blue crabs poured out onto newspaper, you’ve probably had Old Bay seasoning. It’s a blend of celery salt, black pepper, crushed red-pepper flakes and paprika, and any member of its fiercely loyal Mid-Atlantic fan base will tell you that it should be present at any proper crab or shrimp boil. In this recipe, you get lots of that seaside flavor without having to source fresh blue crab.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image14.jpeg",
        user_id=1
    )

    camambert = Recipe(
        title="Dutch Baby With Bacon and Runny Camembert",
        time_to_cook="40 mins",
        description="Most Dutch babies are sweet and often fruity. Not this one, which is topped with runny Camembert cheese and studded with bacon. It’s savory, golden and perfect for a hardy brunch or light dinner. A word of caution: It deflates quickly, so be sure to serve it as soon as it comes out of the oven.",
        servings=2,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image15.jpeg",
        user_id=1
    )

    chebureki = Recipe(
        title="Chebureki",
        time_to_cook="4 hours",
        description="Chebureki are the southern Ukrainian branch of the global family of empanadas, potstickers, pasties and salteñas — dough pockets filled with meat and deep-fried until golden and juicy. A blistered, chewy crust is the sign of a really good cheburek according to Olga Koutseridi, who grew up in Mariupol, Ukraine, and adapted this recipe for her home kitchen in Austin, Texas. ",
        servings=12,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image16.jpeg",
        user_id=2
    )

    pork_chops = Recipe(
        title="Pan-Fried Breaded Pork Chops",
        time_to_cook="30 mins",
        description="Look for beautiful good-quality pork, such as Berkshire, and ask for center-cut loin chops with bone. Make sure to fry these chops very gently over medium-high heat, to allow the bread-crumb coating to brown slowly, creating a crisp, golden crust. Serve with a tart salad or braised greens, such as broccoli rabe.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image17.jpeg",
        user_id=3
    )

    pancakes = Recipe(
        title="Chez Ma Tante’s Pancakes",
        time_to_cook="20 mins",
        description="At the Brooklyn restaurant Chez Ma Tante, the brunch pancakes come two to an order, big as dessert plates and almost burnt. “I knew I wanted them to be really, really crispy,” said the chef de cuisine Jake Leiber. ",
        servings=8,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image18.jpeg",
        user_id=4
    )

    flan = Recipe(
        title="Zucchini Flan",
        time_to_cook="1 hour",
        description="Zucchini flan makes a good brunch, lunch or light supper dish. For the best texture, be careful not to overbake; remove from the oven when the custard is still a little jiggly. The flan tastes best served at room temperature.",
        servings=6,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image19.jpeg",
        user_id=5
    )

    pavlova = Recipe(
        title="Dessert 'Pavlova'",
        time_to_cook="2 hours 15 minutes",
        description="This Pavlova is a perfect dessert, crisp on the outside with marshmallowy goodness on the inside, piled high with fluffy cream and loads of fresh fruit.",
        servings=15,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image20.jpg",
        user_id=6
    )

    pasta_chicken = Recipe(
        title="Rasta Pasta With Jerk Chicken",
        time_to_cook="45 mins",
        description="Comforting and spicy in just the right way, Rasta pasta is popular in Jamaican communities across New York and beyond. This version gets its spice from jerk seasoning and a single Scotch bonnet.",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image21.jpeg",
        user_id=1
    )

    lemony_shrimp = Recipe(
        title="Lemony Shrimp and Bean Stew",
        time_to_cook="30 mins",
        description="With minimal prep and a quick cook time, this shrimp stew feels elegant for such an easy weeknight meal. You can also take the dish in a number of directions: Substitute the shrimp with an equal amount of flaky white fish or even seared scallops, or stretch the dish into a meal for six by stirring in some butter and serving over cooked spaghetti or rigatoni. A good glug of your best olive oil would also be a welcome.image22",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image22.jpeg",
        user_id=1
    )

    key_lime_pie = Recipe(
        title="Key Lime Pie",
        time_to_cook="30 mins",
        description="Key limes are small, yellowish, seedy and wildly more tart than their ordinary Persian counterparts. Unfortunately, Key limes grow slowly, so many Florida farmers replaced their Key lime trees with Persian ones. You can buy bottled Key lime juice at most supermarkets, but you can also make this easy pie with regular limes, although it won't be quite as delightfully tart.",
        servings=8,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image23.jpeg",
        user_id=8
    )

    guacamole = Recipe(
        title="Chile Verde Guacamole",
        time_to_cook="30 mins",
        description="Mexicans are split into two camps when it comes to guacamole: those who always add lime juice and those who absolutely do not. Many Sonoran friends shout “Never!” at the mere suggestion. Having grown up in the pro-lime camp in Mexico City, I was filled with skepticism before trying versions from the deep Mexican north, but what a pleasant surprise. (I hate to admit it, but this guacamole really needs no lime.)",
        servings=6,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image24.jpeg",
        user_id=7
    )

    swordfish = Recipe(
        title="Grilled Marinated Swordfish Steaks",
        time_to_cook="30 mins",
        description="Swordfish, with its firm, lean flesh, is an ideal candidate for grilling. It's not as forgiving as some fatty fish, like tuna and black sea bass, so proceed with caution. If you remove the fish from the fire when the center is still slightly pink, by the time it gets to the table it should be cooked through. ",
        servings=4,
        img_url="https://theonlychefsbook.s3.us-west-1.amazonaws.com/image25.jpeg",
        user_id=10
    )

    yogurt_chicken = Recipe(
        title="Yogurt-Marinated Fried Chicken With Saffron and Paprika",
        time_to_cook="45 mins",
        description="Here is a fried chicken recipe that is the best kind of weeknight cooking, with ingredients found quickly at most local grocery stores, whirled in a food processor and then left overnight to turn into something delicious the next evening.",
        servings=8,
        img_url="26",
        user_id=11
    )

    greek_tomato_salad = Recipe(
        title="Greek Tomato Salad",
        time_to_cook="20 mins",
        description="The Greek approach to a good tomato salad, whether it has cucumbers and lettuce or not (this one doesn’t), is all about keeping it simple. Sweet, ripe summer tomatoes, salt and olive oil are all you need. The flourishes here — green pepper, red onion, chopped mint and pinch of oregano — are optional, but they add brightness. Good Greek feta cheese takes it over the top.",
        servings=6,
        img_url="27",
        user_id=12
    )

    rainbow_beef = Recipe(
        title="Rainbow Beef",
        time_to_cook="20 mins",
        description="In this version of a stir-fry classic I am using less beef than a typical recipe would call for and adding in some shiitake mushrooms and extra peppers.",
        servings=4,
        img_url="28",
        user_id=13
    )

    mac_cheese = Recipe(
        title="Creamy Macaroni and Cheese",
        time_to_cook="1 hour\n40 mins",
        description="This creamy version has one powerful advantage for the cook: There’s no need to preboil the pasta. It cooks in the oven, absorbing the liquid from the dairy products.",
        servings=8,
        img_url="29",
        user_id=1
    )

    lava_cake = Recipe(
        title="Chocolate Lava Cake for Two",
        time_to_cook="25 mins",
        description="Chocolate lava cakes gained popularity in the late 1990s thanks to the chef Jean-Georges Vongerichten, and they have stuck around on dessert menus for good reason: They are rich chocolate cake and velvety sauce all in one, and they are surprisingly easy to make in under an hour. ",
        servings=2,
        img_url="30",
        user_id=5
    )

    db.session.add(crab_cheddar_quiche)
    db.session.add(autumn_cheesecake)
    db.session.add(beer_steak)
    db.session.add(watermelon_lemonade)
    db.session.add(parmesan_chicken)
    db.session.add(creamy_shrimp)
    db.session.add(seared_tuna)
    db.session.add(grilled_jalapeno)
    db.session.add(miso_soup)
    db.session.add(quick_qiuiche)
    db.session.add(orange_beef)
    db.session.add(mousse_bars)
    db.session.add(watermelon_salad)
    db.session.add(corn)
    db.session.add(camambert)
    db.session.add(chebureki)
    db.session.add(pork_chops)
    db.session.add(pancakes)
    db.session.add(flan)
    db.session.add(pavlova)
    db.session.add(pasta_chicken)
    db.session.add(lemony_shrimp)
    db.session.add(key_lime_pie)
    db.session.add(guacamole)
    db.session.add(swordfish)
    db.session.add(yogurt_chicken)
    db.session.add(greek_tomato_salad)
    db.session.add(rainbow_beef)
    db.session.add(mac_cheese)
    db.session.add(lava_cake)
    db.session.commit()


def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()
