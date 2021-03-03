"""Game: Is number even or not."""
import random

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

# Range of random number
MIN, MAX = 1, 100


def is_even(number):
    """Return True if number is even else False.

    Args:
        number: number to check

    Returns:
        bool
    """
    return bool(number % 2 == 0)


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    question = str(random.randint(MIN, MAX))
    correct_answer = 'yes' if is_even(int(question)) else 'no'
    return question, correct_answer
