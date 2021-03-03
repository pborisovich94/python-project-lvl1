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


def print_to_user(text):
    """Print information to user.

    Args:
        text: information to be printed out to user
    """
    print(text)


def play(game):
    """Plays the game.

    Args:
        game: certain game
    """
    # СНАЧАЛА ПРИВЕТСТВУЕМ ИГРОКА
    print_to_user(constants.INTRODUCTION)

    # Далее спрашиваем имя игрока и приветствуем его
    user_name = prompt.string(
        '{text} '.format(text=constants.PROMPT_FOR_NAME),
    )
    print_to_user('{text}, {user_name}!'.format(
        text=constants.GREETING, user_name=user_name,
    ))

    # Далее выводим правила игры
    print_to_user('{rules}'.format(rules=game.GAME_RULES))

    # Далее идёт цикл на верный/неверный ответ
    for _ in range(0, constants.LOOPS_FOR_WIN):
        (question, correct_answer) = game.get_question_and_correct_answer()
        print_to_user('{question}: {number}'.format(
            question=constants.PROMPT_FOR_QUESTION,
            number=question,
        ))
        user_answer = ask_user()
        if user_answer == correct_answer:
            print_to_user('{text}'.format(text=constants.CASE_CORRECT))
        else:
            print_to_user(
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
    else:
        print_to_user('{text}, {user_name}!'.format(
            text=constants.CONGRATULATION,
            user_name=user_name,
        ))
