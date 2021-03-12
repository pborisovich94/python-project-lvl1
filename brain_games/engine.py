"""Game engine."""
import prompt


def play(game):
    """Plays the game.

    Args:
        game: certain game
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=user_name))
    print('{rule}'.format(rule=game.GAME_RULE))

    loops_for_win = 3
    for _ in range(0, loops_for_win):
        (question, correct_answer) = game.get_question_and_correct_answer()
        print('Question: {number}'.format(number=question))
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(
                "'{user_answer}' is wrong answer ;(. ".format(
                    user_answer=user_answer,
                )
                + "Correct answer was '{correct_answer}'.\n".format(
                    correct_answer=correct_answer,
                )
                + "Let's try again, {user_name}!".format(
                    user_name=user_name,
                ),
            )
            return
        print('Correct!')

    print('Congratulations, {user_name}!'.format(user_name=user_name))
