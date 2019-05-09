"""Execute a crossword game."""
from importdata import read_json_data
from crossword import Crossword


def main():
    """App entry point."""
    puzzle = read_json_data('./data/crossword.json')
    words = read_json_data('./data/words.json')
    crossword_game = Crossword(puzzle, words)
    result = crossword_game.find_words()
    return result


if __name__ == "__main__":
    print(main())
