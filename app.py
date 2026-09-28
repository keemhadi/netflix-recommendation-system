"""Web interface for the Netflix recommendation system."""

from flask import Flask, render_template, request

from main import CONTENT_TYPES, GENRES, LANGUAGES, get_recommendations


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Display the preference form and matching recommendations."""
    selections = {
        "content_type": "",
        "genre": "",
        "language": "",
    }
    recommendations = None
    error = None

    if request.method == "POST":
        selections = {
            "content_type": request.form.get("content_type", ""),
            "genre": request.form.get("genre", ""),
            "language": request.form.get("language", ""),
        }

        valid_selection = (
            selections["content_type"] in CONTENT_TYPES
            and selections["genre"] in GENRES
            and selections["language"] in LANGUAGES
        )

        if valid_selection:
            recommendations = get_recommendations(
                selections["content_type"],
                selections["genre"],
                selections["language"],
            )
        else:
            error = "Please select a valid option from every menu."

    return render_template(
        "index.html",
        content_types=CONTENT_TYPES,
        genres=GENRES,
        languages=LANGUAGES,
        selections=selections,
        recommendations=recommendations,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
