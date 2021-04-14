from configparser import ConfigParser
from books_api.database.models.book import Book
from books_api import database_service
import requests
import logging


class ExternalApiService:
    """encapsulates the google API connection"""

    def __init__(self):

        config_object = ConfigParser()
        config_object.read("books_api/config.ini")

        self.api_url = config_object['GOOGLECONFIG']['url']

    def get_data(self, query: str) -> list:
        """sends a request to the api and returns a list of internal models"""

        params = {'q': query}
        raw_response = requests.get(self.api_url, params=params)
        if raw_response.ok:

            result = self.__parse_request_to_books(raw_response.json())

        return result

    def __parse_request_to_books(self, raw_response: dict) -> list:
        """parses the data from json to internal book model"""
        books_list = raw_response['items']
        result = []

        for book in books_list:

            logging.info(book)
            if 'categories' in book['volumeInfo']:
                categories = [database_service.get_category(category) for category in book['volumeInfo']['categories']]
            else:
                categories = []
            authors = [database_service.get_author(author) for author in book['volumeInfo']['authors']]
            average_rating = book['volumeInfo'].get('averageRating', -1)  # TODO Consider making this a None or "NA"
            ratings_count = book['volumeInfo'].get('ratingsCount', 0)
            thumbnail =  book['volumeInfo'].get('imageLinks')
            if thumbnail:
                thumbnail = thumbnail.get('thumbnail')

            new_book = Book(book['id'], book['volumeInfo']['title'], authors, categories,book['volumeInfo']['publishedDate'],
                            average_rating, ratings_count, thumbnail)

            result.append(new_book)

        return result


