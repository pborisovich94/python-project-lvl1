"""Is it a prime number?."""
import random

GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def _is_prime(number):
    """Return True if number is prime else False.

    Args:
        number: number for check

    Returns:
        bool
    """
    if number <= 1:
        return False

    div = 2
    while number % div != 0:
        div += 1
    return div == number


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    number = random.randint(1, 100)
    correct_answer = 'yes' if _is_prime(number=number) else 'no'
    question = '{number}'.format(number=number)
    return question, correct_answer
