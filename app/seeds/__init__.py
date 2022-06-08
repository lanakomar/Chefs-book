from flask.cli import AppGroup
from .users import seed_users, undo_users
from .ingredients import seed_ingredients, undo_ingredients
from .instructions import seed_instructions, undo_instructions
from .measurement_units import seed_measurement_units, undo_measurement_units
from .recipes import seed_recipes, undo_recipes
from .notes import seed_notes, undo_notes


# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_recipes()
    seed_measurement_units()
    seed_ingredients()
    seed_instructions()
    seed_notes()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_measurement_units()
    undo_users()
    undo_recipes()
    undo_ingredients()
    undo_instructions()
    undo_notes()
