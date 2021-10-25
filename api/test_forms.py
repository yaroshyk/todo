import unittest

from django.utils.timezone import now

from api.forms import TodoForm


class FormTestCase(unittest.TestCase):
    def test_TodoForm_required(self):
        """Validate required fields"""
        form = TodoForm(
            data={"title": "Title",
                  "group": "0",
                  "details": "Details",
                  "date": now(),
                  "user_id": 3}
        )

        self.assertEqual(form.is_valid(), True, "Optional field was marked as required")

    def test_TodoForm_missing_required(self):
        """Validate required fields"""
        form = TodoForm(
            data={"group": "0",
                  "details": "Details",
                  "date": now(),
                  "user_id": 3}
        )

        self.assertEqual(form.is_valid(), False, 'Required field "title" no longer required')


if __name__ == '__main__':
    unittest.main()
