# Program Design

## Purpose

The program recommends Netflix-style titles based on three user preferences. The same recommendation logic is available through a console interface and a simple Flask web interface.

## Inputs

1. Content type: Movie or Series
2. Genre: Action, Comedy, Drama, or Science Fiction
3. Language: English, Korean, or Spanish

In the console, the user enters a number for each menu. On the web page, the user selects values from dropdown menus. Invalid entries display an error message.

## Processing

The program compares the selected content type, genre, and language with every item in the catalogue. An item is included only when all three values match.

## Outputs

The program displays the matching title or a message stating that no match was found. The console asks whether the user wants to search again, while the web form remains available for another search.

## Test cases

| Test | Input or condition | Expected result |
| --- | --- | --- |
| Movie match | Movie, Action, English | The Last Mission |
| Series match | Series, Comedy, Korean | Laughing Together |
| No match | Movie, Horror, English | Empty result |
| Invalid menu input | `wrong`, `5`, then `2` | Reject first two entries and accept Series |
| Invalid continue input | `maybe`, then `yes` | Reject first entry and continue |

Automated versions of these cases are stored in `tests/test_main.py` and `tests/test_app.py`.

## Evidence for the report

Save screenshots of the following in `evidence/screenshots/`:

1. The source code in `main.py` and `data.py`.
2. A successful recommendation in the console.
3. An invalid entry followed by a valid entry.
4. The successful automated test output.
5. The output of `git log --oneline --graph`.
6. The recommendation web page in a browser.
