from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from books_api.database.database_service import Base
from books_api.database.models.association_tables import book_to_author


class Author(Base):

    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    books = relationship("Book", secondary=book_to_author, back_populates="authors")

    def __init__(self, name):
        self.name = name







