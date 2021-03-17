"""Game: Calculator."""
import operator as operator_module
import random

GAME_RULE = 'What is the result of the expression?'


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operators = {
        '+': operator_module.add,
        '-': operator_module.sub,
        '*': operator_module.mul,
    }

    operator = random.choice(list(operators.keys()))

    question = f'{operand1} {operator} {operand2}'
    correct_answer = str(operators[operator](operand1, operand2))

    return question, correct_answer
