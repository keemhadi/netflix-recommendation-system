# Netflix Recommendation System

A simple interactive Python recommendation system for a university assignment. It can run in the terminal or as a small web application.

## Features

- Choose between a movie and a series.
- Choose a genre.
- Choose a language.
- Display matching recommendations.
- Handle invalid input clearly.
- Allow the user to request another recommendation.

## Install the web dependency

From the project folder, run:

```text
python -m pip install -r requirements.txt
```

## Run the web application

```text
python app.py
```

Open `http://127.0.0.1:5000` in a web browser. Stop the server by pressing `Ctrl+C` in the terminal.

## Run the console application

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
- `app.py` - Flask web application
- `data.py` - movie and series catalogue
- `templates/` - web page template
- `static/` - web page styling
- `docs/` - assignment notes and supporting documentation
- `tests/` - automated tests for recommendations and invalid input

## Development approach

Features were added in small stages with a separate Git commit for each meaningful change.
