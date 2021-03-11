"""Even game script."""

from brain_games.engine import play
from brain_games.games import brain_even


def main():
    """Play the game: Is number even or not."""
    play(brain_even)


if __name__ == '__main__':
    main()
