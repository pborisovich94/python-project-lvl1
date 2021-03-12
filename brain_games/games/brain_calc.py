"""Game: Calculator."""
import operator as operator_module
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

    Raises:
        ValueError: unknown incoming operator
    """
    operand1 = random.randint(MIN, MAX)
    operator = random.choice([ADDITION, SUBTRACTION, MULTIPLICATION])
    operand2 = random.randint(MIN, MAX)

    question = '{operand1} {operator} {operand2}'.format(
        operand1=operand1,
        operator=operator,
        operand2=operand2,
    )

    if operator == ADDITION:
        correct_answer = str(operator_module.add(operand1, operand2))
    elif operator == SUBTRACTION:
        correct_answer = str(operator_module.sub(operand1, operand2))
    elif operator == MULTIPLICATION:
        correct_answer = str(operator_module.mul(operand1, operand2))
    else:
        raise ValueError('Unknown operator: {operator}'.format(
            operator=operator,
        ))

    return question, correct_answer
