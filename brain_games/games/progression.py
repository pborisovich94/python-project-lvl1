"""Game: Progression."""
import random

GAME_RULE = 'What number is missing in the progression?'

# Progression length
LENGTH = 10

# First number of progression
FIRST_MIN, FIRST_MAX = 1, 20

# Progression step
STEP_MIN, STEP_MAX = 3, 50


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    first = random.randint(FIRST_MIN, FIRST_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    missed = random.randint(0, LENGTH - 1)

    progression = [str(first + step * num) for num in range(LENGTH)]
    correct_answer = str(progression[missed])
    progression[missed] = '..'
    question = ' '.join(progression)
    return question, correct_answer
