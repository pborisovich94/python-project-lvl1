"""Game engine."""
import prompt
from brain_games import constants


def ask_user():
    """Ask user to provide answer.

    Returns:
        str
    """
    return prompt.string(
        '{text}: '.format(text=constants.PROMPT_FOR_ANSWER),
    )


def play(game):
    """Plays the game.

    Args:
        game: certain game
    """
    print(constants.INTRODUCTION)

    user_name = prompt.string(
        '{text} '.format(text=constants.PROMPT_FOR_NAME),
    )
    print('{text}, {user_name}!'.format(
        text=constants.GREETING, user_name=user_name,
    ))

    print('{rules}'.format(rules=game.GAME_RULES))

    for _ in range(0, constants.LOOPS_FOR_WIN):
        (question, correct_answer) = game.get_question_and_correct_answer()
        print('{question}: {number}'.format(
            question=constants.PROMPT_FOR_QUESTION,
            number=question,
        ))
        user_answer = ask_user()
        if user_answer != correct_answer:
            print(
                "'{user_answer}' {text}. ".format(
                    user_answer=user_answer,
                    text=constants.CASE_INCORRECT_WRONG,
                )
                + "{text} '{correct_answer}'.\n".format(
                    text=constants.CASE_INCORRECT_EXPECTED,
                    correct_answer=correct_answer,
                )
                + '{text}, {user_name}!'.format(
                    text=constants.CASE_INCORRECT_REPEAT,
                    user_name=user_name,
                ),
            )
            break
        print('{text}'.format(text=constants.CASE_CORRECT))

    print('{text}, {user_name}!'.format(
        text=constants.CONGRATULATION,
        user_name=user_name,
    ))
