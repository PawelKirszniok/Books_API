from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import logging

Base = declarative_base()

from books_api.database.models.book import Book
from books_api.database.models.author import Author
from books_api.database.models.category import Category


class DatabaseService:
    """encapsulates and manages the internal database connection

    proper use of the DatabaseService requires starting a query with get_all_books. Filtering it using any number of
    filter methods and then finally sorting it with the sort_books method """

    def __init__(self):

        config_object = ConfigParser()
        config_object.read("books_api/config.ini")

        db_config = config_object['DATABASECONFIG']
        login_string = f"{db_config['prefix']}://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['dbname']}"

        self.engine = create_engine(login_string, pool_pre_ping=True)

        self.session = sessionmaker(bind=self.engine)()

    def get_book(self, book_id: str) -> Book:
        search = self.session.query(Book).filter_by(id=book_id).all()

        if not len(search):
            return None
        else:
            return search[0]

    def get_all_books(self):
        search = self.session.query(Book)

        return search

    def filter_by_year(self, books, year_filter: int):
        """filters only books from a specific year from the provided list

        :param books: sqlalchemy query object
        :param year_filter: the publication year to filter to
        :return: filtered query object
        """
        return books.filter_by(published_date=year_filter)

    def sort_books(self, books,  sort_by_years: int = 0) -> list:
        """returns a list of books dependent on publication date

        :param books: query object returned by other functions of this class
        :param sort_by_years: 1 for ascending, 0 for no sorting, -1 for descending
        :return: sorted list of all books matching the criteria
        """
        if sort_by_years == 1:
            return books.order_by(Book.published_date.asc())

        elif sort_by_years == -1:
            return books.order_by(Book.published_date.desc())

        else:
            return books.all()

    def filter_by_author(self, books, authors: list):
        """returns a list of books written by the authors provided.

        if there are multiple authors the result includes all books written by all of them ( a product of the sets)

        :param books: query object to be manipulated
        :param authors: list of authors
        :return: filtered query object
        """
        for author in authors:
            search = self.session.query(Author).filter_by(name=author).all()
            logging.info(search)
            if search:
                books = books.filter(Book.authors.contains(search[0]))

        return books

    def get_category(self, category_name:str) -> Category:
        """returns a category object that can be assigned to a book"""
        search = self.session.query(Category).filter_by(name=category_name).all()
        if search:
            return search[0]
        else:
            new_category = Category(category_name)
            self.session.add(new_category)
            return new_category

    def get_author(self, author_name:str) -> Author:
        """returns an author object that can be assigned to a book"""
        search = self.session.query(Author).filter_by(name=author_name).all()
        if search:
            return search[0]
        else:
            new_author = Author(author_name)
            self.session.add(new_author)
            return new_author

    def update_data(self, data_to_save: list):
        """saves a list of book objects to the database"""

        for book in data_to_save:

            if self.get_book(book.id):
                book = self.session.merge(book)

            self.session.add(book)

        self.session.commit()