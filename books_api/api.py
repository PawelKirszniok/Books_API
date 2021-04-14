from flask import Flask
from flask_restful import Api
from books_api.endpoints.update_data import UpdateData
from books_api.endpoints.get_book import GetBook
from books_api.endpoints.get_books import GetBooks

app = Flask(__name__)
api = Api(app)

api.add_resource(UpdateData, "/db")
api.add_resource(GetBook, "/books/<string:book_id>")
api.add_resource(GetBooks, "/books")