"""Game engine."""
import prompt


def play(game):
    """Plays the game.

    Args:
        game: certain game
    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.GAME_RULE)

    game_rounds_count = 3
    for _ in range(0, game_rounds_count):
        question, correct_answer = game.get_question_and_correct_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                + f"Correct answer was '{correct_answer}'.\n"
                + f"Let's try again, {user_name}!",
            )
            return
        print('Correct!')

    print(f'Congratulations, {user_name}!')
