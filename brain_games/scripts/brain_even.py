"""Even game script."""
import random
import prompt


INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
PROMPT_FOR_QUESTION = 'Question: '
PROMPT_FOR_ANSWER = 'Your answer: '
CASE_CORRECT = 'Correct!'
CASE_INCORRECT_WRONG = ' is wrong answer ;(. '
CASE_INCORRECT_EXPECTED = 'Correct answer was '
CASE_INCORRECT_REPEAT = "Let's try again, "
CONGRATULATION = 'Congratulations, '


def is_even(number):
    """Return True if number is even else False.

    Args:
        number: number to check

    Returns:
        bool
    """
    return bool(number % 2 == 0)


def welcome_user():
    """Ask users name and welcomes him/her.

    Returns:
        user_name
    """
    user_name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=user_name))
    return user_name


def play_even(user_name):
    """Generate questions and correct_answers.

    Args:
        user_name: playing player name
    """
    print(INSTRUCTION)
    wins = 0

    while wins < 3:
        target = random.randint(1, 100)
        print(PROMPT_FOR_QUESTION + str(target))
        user_answer = prompt.string(PROMPT_FOR_ANSWER)
        correct_answer = 'yes' if target % 2 == 0 else 'no'

        if (is_even(target) and user_answer == 'yes') or (not is_even(target) and user_answer == 'no'):
            print(CASE_CORRECT)
            wins += 1
            if wins == 3:
                print(CONGRATULATION + user_name + '!')
        else:
            print('"' + user_answer + '"' + CASE_INCORRECT_WRONG, end='')
            print(CASE_INCORRECT_EXPECTED + '"' + correct_answer + '"')
            print(CASE_INCORRECT_REPEAT + user_name + '!')
            break


def main():
    """Welcomes user and ask his name."""
    print('Welcome to the Brain Games!')
    user_name = welcome_user()
    play_even(user_name)


if __name__ == '__main__':
    main()
