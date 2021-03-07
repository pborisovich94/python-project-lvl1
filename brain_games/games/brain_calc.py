"""Game: Calculator."""
import random

GAME_RULES = 'What is the result of the expression?'

# Range of random number
MIN, MAX = 1, 100

# Operators
ADDITION, SUBTRACTION, MULTIPLICATION = '+', '-', '*'


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    question = '{operand_1} {operator} {operand_2}'.format(
        operand_1=str(random.randint(MIN, MAX)),
        operator=random.choice([ADDITION, SUBTRACTION, MULTIPLICATION]),
        operand_2=str(random.randint(MIN, MAX)),
    )
    correct_answer = str(eval(question))
    return question, correct_answer
