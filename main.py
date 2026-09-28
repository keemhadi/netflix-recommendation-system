"""Interactive Netflix recommendation system."""

from data import TITLES


CONTENT_TYPES = ["Movie", "Series"]
GENRES = ["Action", "Comedy", "Drama", "Science Fiction"]
LANGUAGES = ["English", "Korean", "Spanish"]


def get_recommendations(content_type, genre, language):
    """Return titles that match all three user preferences."""
    return [
        item
        for item in TITLES
        if item["type"] == content_type
        and item["genre"] == genre
        and item["language"] == language
    ]


def get_menu_choice(prompt, options):
    """Display a numbered menu and keep asking until the input is valid."""
    print(f"\n{prompt}")
    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice_number = int(choice)
            if 1 <= choice_number <= len(options):
                return options[choice_number - 1]

        print(f"Invalid choice. Please enter a number from 1 to {len(options)}.")


def display_recommendations(recommendations):
    """Display the matching title recommendations."""
    print("\nYour recommendation:")

    if not recommendations:
        print("No matching titles were found.")
        return

    for item in recommendations:
        print(f'- {item["title"]}')


def ask_to_continue():
    """Ask whether the user wants another recommendation."""
    while True:
        answer = input("\nWould you like another recommendation? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Invalid choice. Please enter y or n.")


def main():
    """Run the interactive recommendation program."""
    print("=" * 42)
    print("     NETFLIX RECOMMENDATION SYSTEM")
    print("=" * 42)

    while True:
        content_type = get_menu_choice("Choose a content type:", CONTENT_TYPES)
        genre = get_menu_choice("Choose a genre:", GENRES)
        language = get_menu_choice("Choose a language:", LANGUAGES)

        recommendations = get_recommendations(content_type, genre, language)
        display_recommendations(recommendations)

        if not ask_to_continue():
            print("\nThank you for using the recommendation system!")
            break


if __name__ == "__main__":
    main()
