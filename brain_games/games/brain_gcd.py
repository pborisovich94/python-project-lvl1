"""Game: GCD."""
import random

GAME_RULES = 'Find the greatest common divisor of given numbers.'

# Range of random number
MIN, MAX = 1, 100


def find_gcd(number1, number2):
    """Find the greatest common divisor of given numbers.

    Args:
        number1: first number
        number2: second number

    Returns:
        int
    """
    possible_gcd = number1 if number1 < number2 else number2

    for num in reversed(range(possible_gcd + 1)):
        gcd_n1 = number1 % num
        gcd_n2 = number2 % num
        if gcd_n1 == 0 and gcd_n2 == 0:
            return num


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    number1 = random.randint(MIN, MAX)
    number2 = random.randint(MIN, MAX)
    question = '{number_1} {number_2}'.format(
        number_1=str(number1),
        number_2=str(number2),
    )
    correct_answer = str(find_gcd(number1=number1, number2=number2))
    return question, correct_answer
