from sqlalchemy import String, Integer, Column, Float
from sqlalchemy.orm import relationship
from books_api.database.database_service import Base
from books_api.database.models.association_tables import book_to_author, book_to_category


class Book(Base):

    __tablename__ = "book"
    id = Column(String(20), primary_key=True)
    title = Column(String(200), nullable=False)
    authors = relationship("Author", secondary=book_to_author, back_populates="books")
    categories = relationship("Category", secondary=book_to_category, back_populates="books")
    published_date = Column(Integer, nullable=False)
    average_rating = Column(Float)
    ratings_count = Column(Integer)
    thumbnail = Column(String(1000))

    def __init__(self, id, title, authors, categories, published_date, average_rating, ratings_count, thumbnail):

        self.id = id
        self.title = title
        self.authors = authors
        self.categories = categories
        self.published_date = published_date
        self.average_rating = average_rating
        self.ratings_count = ratings_count
        self.thumbnail = thumbnail

    def to_json(self) -> dict:
        """creates a dictionary to conform to the required format below
    {
    "title": "Hobbit czyli Tam i z powrotem",
    "authors": ["J. R. R. Tolkien"],
    "published_date": "2004",
    "categories": [
        "Baggins, Bilbo (Fictitious character)"
      ],
    "average_rating": 5,
    "ratings_count": 2,
    "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api",
    }"""
        authors = [author.name for author in self.authors]
        categories = [category.name for category in self.categories]

        result = {'title': self.title,
                  'authors': authors,
                  'categories': categories,
                  'published_date': self.published_date,
                  'average_rating': self.average_rating,
                  'ratings_count': self.ratings_count,
                  'thumbnail': self.thumbnail}

        return result






