from app.models import db, User, Ingredient, Recipe



# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password')

    pelicangal = User(
        username='pelicangal', email='pelicangal@aa.io', password='1lovese@food')

    gordon_ramsay = User(
        username='gordon_ramsay', email='gordon_ramsay@aa.io', password='1amTheBest@cooking!')

    mary = User(
        username='Mary', email='mary@gmail.com', password='B@n@n@Mi1lk')

    banana_milk = User(
        username='banana_milk', email='banana_milk@yahoo.com', password='1amTheBest@!')

    boba_fett = User(
        username='boba_fett', email='boba_fett@aa.io', password='bob@Fett2!')

    guy_fieri = User(
        username='guy_fieri', email='guy_fieri@gmail.com', password='superSTRONGpassword1!')

    jamie_oliver = User (
        username = 'jamie_oliver', email='jamie_oliver@gmail.com', password='!Host@TheNakedChef1')

    martha_stewart = User (
        username = 'martha_stewart', email='martha_stewart@gmail.com', password='!Host@TMarthaKnowsBest1')

    rachel_ray = User (
        username = 'rachel_ray', email='rachel_ray@gmail.com', password='!Host@30MinutesMeals')

    james_t_kirk = User (
        username = 'james_t_kirk', email='james_t_kirk@aa.com', password='!james!t!kirk1')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(pelicangal)
    db.session.add(gordon_ramsay)
    db.session.add(mary)
    db.session.add(banana_milk)
    db.session.add(boba_fett)
    db.session.add(guy_fieri)
    db.session.add(jamie_oliver)
    db.session.add(martha_stewart)
    db.session.add(rachel_ray)
    db.session.add(james_t_kirk)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
