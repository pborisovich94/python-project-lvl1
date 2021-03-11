"""Progression game script."""

from brain_games.engine import play
from brain_games.games import brain_progression


def main():
    """Play the game: Progression."""
    play(brain_progression)


if __name__ == '__main__':
    main()
