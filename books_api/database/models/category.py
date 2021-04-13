from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from books_api.database.database_service import Base
from books_api.database.models.association_tables import book_to_category


class Category(Base):

    __tablenamme__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    books = relationship("Book", secondary=book_to_category, back_populates="categories")

    def __init__(self, name):
        self.name = name










