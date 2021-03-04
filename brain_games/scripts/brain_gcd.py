"""Greatest common devider game script."""

from brain_games.games import brain_gcd
from brain_games.games.engine import play


def main():
    """Play the game: Greatest common devider."""
    play(brain_gcd)


if __name__ == '__main__':
    main()
