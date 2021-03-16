"""Game: Is number even or not."""
import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def _is_even(number):
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
    question = str(random.randint(1, 100))
    correct_answer = 'yes' if _is_even(int(question)) else 'no'
    return question, correct_answer
