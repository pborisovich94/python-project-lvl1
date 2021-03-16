"""Prime number game script."""

from brain_games.engine import play
from brain_games.games import prime


def main():
    """Play the game: Is it a prime number?."""
    play(prime)


if __name__ == '__main__':
    main()
