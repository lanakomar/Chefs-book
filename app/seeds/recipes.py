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

    db.session.add(crab_cheddar_quiche)
    db.session.commit()


def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()
