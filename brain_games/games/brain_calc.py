"""Game: Calculator."""
import operator as operator_module
import random

GAME_RULES = 'What is the result of the expression?'

# Range of random number
MIN, MAX = 1, 100

# Operators
ADDITION, SUBTRACTION, MULTIPLICATION = '+', '-', '*'


def _calculate(operand1, operator, operand2):
    """Calculate passed expression.

    Args:
        operand1: first number
        operator: "+" or "-" or "*"
        operand2: second number

    Returns:
        str

    Raises:
        ValueError: unknown incoming operator
    """
    if operator == ADDITION:
        return str(operator_module.add(operand1, operand2))
    elif operator == SUBTRACTION:
        return str(operator_module.sub(operand1, operand2))
    elif operator == MULTIPLICATION:
        return str(operator_module.mul(operand1, operand2))
    raise ValueError('Unknown operator: {operator}'.format(
        operator=operator,
    ))


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    operand1 = random.randint(MIN, MAX)
    operator = random.choice([ADDITION, SUBTRACTION, MULTIPLICATION])
    operand2 = random.randint(MIN, MAX)

    question = '{operand1} {operator} {operand2}'.format(
        operand1=operand1,
        operator=operator,
        operand2=operand2,
    )
    correct_answer = _calculate(operand1, operator, operand2)
    return question, correct_answer
