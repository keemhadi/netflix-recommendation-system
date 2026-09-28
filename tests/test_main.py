"""Tests for the Netflix recommendation system."""

import unittest
from unittest.mock import patch

from main import ask_to_continue, get_menu_choice, get_recommendations


class RecommendationTests(unittest.TestCase):
    def test_movie_recommendation_matches_preferences(self):
        results = get_recommendations("Movie", "Action", "English")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "The Last Mission")

    def test_series_recommendation_matches_preferences(self):
        results = get_recommendations("Series", "Comedy", "Korean")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Laughing Together")

    def test_unknown_preferences_return_no_results(self):
        results = get_recommendations("Movie", "Horror", "English")

        self.assertEqual(results, [])

    @patch("builtins.input", side_effect=["wrong", "5", "2"])
    @patch("builtins.print")
    def test_menu_repeats_until_choice_is_valid(self, mock_print, mock_input):
        result = get_menu_choice("Choose:", ["Movie", "Series"])

        self.assertEqual(result, "Series")
        self.assertEqual(mock_input.call_count, 3)

    @patch("builtins.input", side_effect=["maybe", "yes"])
    @patch("builtins.print")
    def test_continue_prompt_handles_invalid_input(self, mock_print, mock_input):
        self.assertTrue(ask_to_continue())
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
