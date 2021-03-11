"""Prime number game script."""

from brain_games.games import brain_prime
from brain_games.engine import play


def main():
    """Play the game: Is it a prime number?."""
    play(brain_prime)


if __name__ == '__main__':
    main()
