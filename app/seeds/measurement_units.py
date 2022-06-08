from app.models import db, Measurement_unit


def seed_measurement_units():
    cups = Measurement_unit(name="cups")
    fluid_ounces = Measurement_unit(name="fluid ounces")
    gallons = Measurement_unit(name="gallons")
    grams = Measurement_unit(name="grams")
    liters = Measurement_unit(name="liters")
    milliliters = Measurement_unit(name="milliliters")
    ounces = Measurement_unit(name="ounces")
    pinch = Measurement_unit(name="pinch")
    pints = Measurement_unit(name="pints")
    pounds = Measurement_unit(name="pounds")
    quarts = Measurement_unit(name="quarts")
    tablespoons = Measurement_unit(name="tablespoons")
    teaspoons = Measurement_unit(name="teaspoons")
    empty = Measurement_unit(name="")
    cans = Measurement_unit(name="cans")
    slices = Measurement_unit(name="slices")
    splash = Measurement_unit(name="splash")

    db.session.add(cups)
    db.session.add(fluid_ounces)
    db.session.add(gallons)
    db.session.add(grams)
    db.session.add(liters)
    db.session.add(milliliters)
    db.session.add(ounces)
    db.session.add(pinch)
    db.session.add(pints)
    db.session.add(pounds)
    db.session.add(quarts)
    db.session.add(tablespoons)
    db.session.add(teaspoons)
    db.session.add(empty)
    db.session.add(cans)
    db.session.add(slices)
    db.session.add(splash)

    db.session.commit()


def undo_measurement_units():
    db.session.execute('TRUNCATE measurement_units RESTART IDENTITY CASCADE;')
    db.session.commit()
