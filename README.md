# Crossword Solver

![Python](https://img.shields.io/badge/python-3.7-blue.svg?longCache=true&style=flat-square&logo=Python&logoColor=fff&colorA=36363e)
![Numpy](https://img.shields.io/badge/numpy-1.16.3-blue.svg?longCache=true&style=flat-square&logo=Python&logoColor=fff&colorA=36363e)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=36363e&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/toddbirchard/crossword-solver.svg?style=flat-square&colorB=daa000&colorA=36363e&logo=GitHub)](https://github.com/toddbirchard/crossword-solver/issues)
[![GitHub Stars](https://img.shields.io/github/stars/toddbirchard/crossword-solver.svg?style=flat-square&colorB=daa000&colorA=36363e&logo=GitHub)](https://github.com/toddbirchard/crossword-solver/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/toddbirchard/crossword-solver.svg?style=flat-square&colorB=FCC624&colorA=36363e&logo=GitHub)](https://github.com/toddbirchard/crossword-solver/network)

*Crossword Solver* finds all words in a crossword puzzle along the vertical or horizontal axises. Results for each word are printed to the console upon script execution. Words will be recognized regardless of being spelled forwards or backwards. Utilizes the Python [NumPy](https://www.numpy.org/) library.

## How To Use

*Crossword Solver* reads from two separate JSON files. These files may be modified to search for different words, or execute a different crossword puzzle entirely:
* `./data/crossword.json` contains the crossword puzzle to be solved.
* `./data/words.json` contains a collection of words to be searched for in the puzzle.

### Installation

**With Pipenv:**

```
$ git clone https://github.com/toddbirchard/crossword-solver
$ cd crossword-solver
$ pipenv update
$ pipenv shell
$ python3 main.py
```

**With Pip:**

```
$ git clone https://github.com/toddbirchard/crossword-solver
$ cd crossword-solver
$ pip3 install -r requirements.txt
$ python3 main.py
```

### Expected Output

Running the script as-is should produce the following result:

```
"how" found in puzzle!
"vue" found in puzzle!
"mope" NOT found in puzzle :(
```
