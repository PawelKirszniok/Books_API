from flask_restful import Resource
from flask import request
from books_api import database_service
import logging


class GetBooks(Resource):
    """Endpoint supporting a GET request that return a list of books processed based on provided parameters """

    def get(self):
        """retrieves and parses the request returning all or filtered books based on args"""

        authors = request.args.getlist('author')
        authors = [author[1:-1] for author in authors]  # Only here to parse quotes added to the request
        year_filter = request.args.get('published_date')
        sort_by = request.args.get('sort')
        sort_by_date = 0
        logging.info(authors)

        if sort_by and 'published_date' in sort_by:
            if sort_by[0] == '-':
                sort_by_date = -1
            else:
                sort_by_date = 1

        intermediate_query = database_service.get_all_books()

        if authors:
            intermediate_query = database_service.filter_by_author(intermediate_query, authors)

        if year_filter:
            intermediate_query = database_service.filter_by_year(intermediate_query, year_filter)

        list_result = database_service.sort_books(intermediate_query, sort_by_date)

        result = []

        for book in list_result:
            result.append(book.to_json())

        return result







