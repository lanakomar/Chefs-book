from xml.dom.expatbuilder import parseFragmentString
from app.models import db, Recipe


def seed_recipes():
    crab_cheddar_quiche = Recipe(
        title="Crab and Cheddar Quiche",
        time_to_cook="55 mins",
        description="Easy crab quiche. Great for any meal or occasion.",
        servings=8,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4524043.jpg",
        user_id=1
    )

    autumn_cheesecake = Recipe(
        title="Autumn Cheesecake",
        time_to_cook="4 hours",
        description="This is a delicious Apple Cheesecake that I usually make in the fall.",
        servings=12,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4556947.jpg",
        user_id=4
    )

    beer_steak = Recipe(
        title="Beer steak",
        time_to_cook="2 hrs 20 mins",
        description="Grilled steak with a simple beer marinade!",
        servings=4,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F697567.jpg",
        user_id=6
    )

    watermelon_lemonade = Recipe(
        title="Refreshing Watermelon Lemonade Slush",
        time_to_cook="50 mins",
        description="Whenever I have excess seasonal fruit, I freeze it in chunks for fast and easy slushes and smoothies. Here's a delicious way to use up some watermelon.",
        servings=2,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F9299867.jpg&w=638&h=848&c=sc&poi=face&q=60",
        user_id=7
    )

    parmesan_chicken = Recipe(
        title="Quick Crispy Parmesan Chicken Breasts",
        time_to_cook="50 mins",
        description="These are delicious, easy, quick, and so versatile! Eat them plain, topped with your favorite spaghetti sauce, or sliced on a Caesar salad.",
        servings=4,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F5938736.jpg",
        user_id=8
    )

    creamy_shrimp = Recipe(
        title="Creamy Shrimp Scampi with Half-and-Half",
        time_to_cook="20 mins",
        description="Dinner doesn't have to take forever--prove it with this fast and delicious shrimp scampi recipe.",
        servings=2,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F43%2F2022%2F04%2F26%2F268669creamy-shrimp-scampi-with-half-and-half-humblepieliving-001-4x3-1.jpg",
        user_id=9
    )

    seared_tuna = Recipe(
        title="Sesame-Seared Tuna",
        time_to_cook="11 mins",
        description="This sesame-seared tuna is an easy, great-tasting dish. Fresh tuna steaks are coated with sesame seeds, then quickly seared and served rare, so be sure to use good quality fresh tuna.",
        servings=4,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F43%2F2022%2F05%2F25%2F869603-sesame-seared-tuna-Scott-K-4x3-1.jpg",
        user_id=10
    )


    grilled_jalapeno = Recipe(
        title="Grilled Jalapeno Poppers",
        time_to_cook="30 mins",
        description="Best poppers you'll have off your grill! Any left over cheese mixture makes a good spread for crackers while you're waiting.",
        servings=16,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F4530082.jpg",
        user_id=9
    )


    miso_soup = Recipe(
        title="Homemade Miso Soup",
        time_to_cook="30 mins",
        description="Make your very own Japanese miso soup from scratch. It's easy to do at home! Perfect for an appetizer or light, warming lunch.",
        servings=4,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F6243395.jpg",
        user_id=11
    )

    quick_qiuiche = Recipe(
        title="Quick Quiche",
        time_to_cook="50 mins",
        description="When you don't have the time to make a pastry crust, try this quick lunch idea. You may add any other goodies you like, such as ham, chicken, crab, shrimp or broccoli.",
        servings=6,
        img_url="https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimages.media-allrecipes.com%2Fuserphotos%2F399957.jpg",
        user_id=10
    )

    # creamy_shrimp = Recipe(
    #     title="",
    #     time_to_cook="20 mins",
    #     description="",
    #     servings=2,
    #     img_url="",
    #     user_id=9
    # )

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
    db.session.commit()


def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()
