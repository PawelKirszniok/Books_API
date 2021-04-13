from flask_restful import Resource, abort
from books_api import database_service


class GetBook(Resource):
    """Endpoint supporting a GET request that will return a single book given the id"""

    def get(self, book_id: str):
        """returns the selected book based on the provided id. For failure states:
        if id not found in the database returns error code 204"""

        book = database_service.get_book(book_id)

        if book:
            return book.to_json()
        else:
            return abort(404, message=f"No books with id {book_id} found")





