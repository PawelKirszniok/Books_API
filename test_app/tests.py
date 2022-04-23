from django.test import TestCase
from test_app.models import Author, Book
from rest_framework.test import APITestCase
from datetime import date
from django.urls import reverse
from test_app.views import AuthorViewSet, BookViewSet


class AuthorTestCase(APITestCase):

    def setUp(self):
        self.author = Author.objects.create(name="J.R.R. Tolkien")
        self.book = Book.objects.create(
            title="Lord of the Rings", author=self.author, publication_date=date(2010, 10, 10)
        )

    def test_get(self):
        url = f'/authors/{self.author.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 1, 'name': 'J.R.R. Tolkien'})


