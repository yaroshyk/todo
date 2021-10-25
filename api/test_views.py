from http import HTTPStatus

from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.utils.timezone import now

from api.models import Todo
from api.views.views import add, remove, edit
from api.views.views import index as index_view


class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_index_view_auth(self):
        """Test registered user index page"""
        # Create an instance of a GET request.
        request = self.factory.get('/')

        # Create User for testing purposes
        user = User.objects.create_user(
            username='jacob', email='jacob@test.case', password='top_secret', id=2)

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = user

        # Test my_view() as if it were deployed at /customer/details
        response = index_view(request)
        # Use this syntax for class-based views.
        #  response = MyView.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<title>TODO LIST</title>", 1)

    def test_index_view_anon(self):
        """Test anonymous user index page"""
        # Create an instance of a GET request.
        request = self.factory.get('/')

        # Or you can simulate an anonymous user by setting request.user to
        # an AnonymousUser instance.
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index_view(request)
        # Use this syntax for class-based views.
        #  response = MyView.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_add_view(self):
        """Test registered user index page"""
        user_id = 3
        # Create an instance of a GET request.
        new_title = "test_add_view Title"
        new_details = "test_add_view Title Details"

        request = self.factory.post('/add', {"title": new_title,
                                             "group": "0",
                                             "details": new_details,
                                             "date": now(),
                                             "user_id": user_id})

        # Create User for testing purposes
        user = User.objects.create_user(
            username='jacob', email='jacob@test.case', password='top_secret', id=user_id)

        # Recall that middleware are not supported. You can simulate a
        # logged-in user by setting request.user manually.
        request.user = user

        # Test my_view() as if it were deployed at /customer/details
        response = add(request)
        # Use this syntax for class-based views.
        #  response = MyView.as_view()(request)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        todo: Todo = Todo.objects.latest('id')

        self.assertEqual(todo.title, new_title)
        self.assertEqual(todo.details, new_details)
        self.assertEqual(todo.user_id, user_id)

    def test_remove(self):
        item_id = 99
        user_id = 9
        Todo.objects.create(
            title="lion",
            user_id=user_id,
            id=item_id)

        user = User.objects.create_user(
            username='jacob', email='jacob@test.case', password='top_secret', id=user_id)

        request = self.factory.delete('/del/<int:item_id>')

        request.user = user

        response = remove(request=request, item_id=item_id)

        self.assertEqual(response.status_code, HTTPStatus.OK, 'No errors in response')
        self.assertEqual(Todo.objects.filter(id=item_id).exists(), False, 'Todo item still exists')

    def test_edit(self):
        item_id = 22
        user_id = 3

        Todo.objects.create(title='Roxi', user_id='3', id=item_id, details="This is old")

        user: User = User.objects.create_user(
            username='roxi', email='roxi@test.case', password='secret_top', id=user_id)

        request = self.factory.post('edit/<int:item_id>', {
            "details": "This is new",
            "title": "Vova",
            "group": "0",
            "date": now(),
            "user_id": user_id
        })

        request.user = user

        response = edit(request, item_id=item_id)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'This is new')
        self.assertNotContains(response, 'This is old')
        self.assertContains(response, 'Vova')
        self.assertNotContains(response, 'Roxi')

        todo = Todo.objects.get(id=item_id)
        self.assertEqual(todo.title, "Vova", 'Title message valid')
        self.assertEqual(todo.details, "This is new", 'Detail message valid')
        self.assertEqual(todo.user_id, user_id, 'Owner of todo is valid')
