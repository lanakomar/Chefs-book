from app.models import db, Note, recipe


def seed_notes():
    db.session.add_all([
        Note(content="I made this, it was great. I added diced baby portabella mushrooms, 1/2 cup diced green onions. It turned out great my family loved it.", date_created="2022-04-15", recipe_id=1, author_id=1),\
        Note(content="Used Monterey Jack cheese instead of cheddar and used whole cream instead of milk. Added extra cheese shreds on top. It was divine!", date_created="2022-01-30", recipe_id=1, author_id=2),\
        Note(content="Another keeper. Modified it a bit by adding mushrooms and green onion. Also, light cream instead of whole milk. Of course, real crab instead of the fake stuff. Easy and simply a good quiche", date_created="2020-11-4", recipe_id=1, author_id=3),\
        Note(content="This came out really good, not too hard or runny. I would maybe cut the parsley back by half.", date_created="2021-08-22", recipe_id=1, author_id=4),\
    ])

    db.session.commit()


def undo_notes():
    db.session.execute('TRUNCATE notes RESTART IDENTITY CASCADE;')
    db.session.commit()
