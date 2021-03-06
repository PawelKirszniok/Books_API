from rest_framework import viewsets
from test_app.serializers import AuthorSerializer, BookSerializer
from test_app.models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


