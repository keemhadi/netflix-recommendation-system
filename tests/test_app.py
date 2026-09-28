"""Tests for the Flask web interface."""

import unittest

from app import app


class WebAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_displays_preference_form(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Netflix Recommendation System", response.data)
        self.assertIn(b"Content type", response.data)

    def test_valid_preferences_display_recommendation(self):
        response = self.client.post(
            "/",
            data={
                "content_type": "Movie",
                "genre": "Action",
                "language": "English",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Last Mission", response.data)

    def test_invalid_preferences_display_error(self):
        response = self.client.post(
            "/",
            data={
                "content_type": "Documentary",
                "genre": "Action",
                "language": "English",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Please select a valid option", response.data)


if __name__ == "__main__":
    unittest.main()
