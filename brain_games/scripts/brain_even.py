"""Even game script."""

from brain_games.games import brain_even
from brain_games.games.engine import play


def main():
    """Play the game: Is number even or not."""
    play(brain_even)


if __name__ == '__main__':
    main()
