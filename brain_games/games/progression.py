"""Game: Progression."""
import random

GAME_RULE = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    """Generate question and correct_answers.

    Returns:
        str,
        str
    """
    first = random.randint(1, 20)
    step = random.randint(3, 50)
    missed = random.randint(0, 10 - 1)

    progression = [str(first + step * num) for num in range(10)]
    correct_answer = str(progression[missed])
    progression[missed] = '..'
    question = ' '.join(progression)
    return question, correct_answer
