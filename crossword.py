"""Execute an instance of a crossword puzzle game."""
import numpy as np


class Crossword:
    """Conduct a crossword search."""

    def __init__(self, puzzle, words):
        """Initialize puzzle with puzzle & word data."""
        self.words = words
        self.puzzle = np.array(puzzle)

    def search_axis_for_word(self, puzzle, word):
        """Search for provided word across a single axis."""
        for axis in puzzle:
            letterMatch = np.intersect1d(axis, word)
            letterMatches = np.asarray(letterMatch).T.tolist()
            if len(letterMatches) == len(word):
                return True
            pass

    def conduct_search(self, word):
        """Search against both rows and columns of puzzle."""
        rowMatch = self.search_axis_for_word(self.puzzle, word)
        columnMatch = self.search_axis_for_word(np.rot90(self.puzzle), word)
        if rowMatch or columnMatch:
            return '"' + ''.join(word) + '" found in puzzle!'
        return '"' + ''.join(word) + '" NOT found in puzzle :('

    def find_words(self):
        """Search puzzle for words."""
        results = "\n".join([self.conduct_search(word) for word in self.words])
        return results
