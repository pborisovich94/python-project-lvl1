"""PLACE FOR DOCSTRING."""
import prompt


def welcome_user():
    """Ask users name and welcomes him/her."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
