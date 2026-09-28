# Netflix Recommendation System

A simple interactive Python console program for a university assignment.

## Features

- Choose between a movie and a series.
- Choose a genre.
- Choose a language.
- Display matching recommendations.
- Handle invalid input clearly.
- Allow the user to request another recommendation.

## How to run

Python 3 is required. From the project folder, run:

```text
python main.py
```

Choose an option by entering the number displayed beside it.

## How to test

Run the automated tests with:

```text
python -m unittest discover -s tests -v
```

## Project structure

- `main.py` - console interaction and recommendation logic
- `data.py` - movie and series catalogue
- `docs/` - assignment notes and supporting documentation
- `evidence/screenshots/` - screenshots of code, output, and Git history
- `tests/` - automated tests for recommendations and invalid input

## Development approach

Features were added in small stages with a separate Git commit for each meaningful change.
