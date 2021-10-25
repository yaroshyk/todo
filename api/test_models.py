from django.test import TestCase

from api.models import Todo


class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title="lion", user_id="1")
        Todo.objects.create(title="cat", user_id="2")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Todo.objects.get(title="lion")
        cat = Todo.objects.get(title="cat")
        self.assertEqual(lion.user_id, 1)
        self.assertEqual(cat.user_id, 2)
