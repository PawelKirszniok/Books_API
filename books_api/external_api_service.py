from configparser import ConfigParser
from books_api.database.models.book import Book
from books_api.database.models.author import Author
from books_api.database.models.category import Category
import requests


class ExternalApiService:
    """encapsulates the google API connection"""

    def __init__(self):

        config_object = ConfigParser()
        config_object.read("TicketingBackground/TicketingSystem/config.ini")

        self.api_url = config_object['GOOGLECONFIG']['url']

    def get_data(self, query: str) -> list:
        """sends a request to the api and returns a list of internal models"""

        params = {'q': query}
        raw_response = requests.get(self.api_url, params=params)
        if raw_response.ok():
            result = self.__parse_request_to_books(raw_response.json())

        return result

    def __parse_request_to_books(self, raw_response: dict) -> list:
        """parses the data from json to internal book model"""
        books_list = raw_response['items']
        result = []

        for book in books_list:

            categories = [Category(category) for category in book['categories']]
            authors = [Author(author) for author in book['authors']]
            average_rating = book.get('averageRating', -1)  # TODO Consider making this a None or "NA"
            ratings_count = book.get('ratingsCount', 0)
            thumbnail = book.get('imageLinks').get('thumbnail')

            new_book = Book(book['id'], book['title'], authors, categories,book['publishedDate'],
                            average_rating, ratings_count, thumbnail)

            result.append(new_book)

        return result


