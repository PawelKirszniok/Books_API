from sqlalchemy import Column, Table, Integer, ForeignKey
from books_api.database.database_service import Base


book_to_author = Table('book_to_author', Base.metadata,
                       Column('book_id', Integer, ForeignKey('book.id')),
                       Column('author_id', Integer, ForeignKey('author.id')))

book_to_category = Table('book_to_category', Base.metadata,
                         Column('book_id', Integer, ForeignKey('book.id')),
                         Column('category_id', Integer, ForeignKey('category.id')))
