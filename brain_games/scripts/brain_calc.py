"""Calculator game script."""

from brain_games.engine import play
from brain_games.games import brain_calc


def main():
    """Play the game: Calculator."""
    play(brain_calc)


if __name__ == '__main__':
    main()
