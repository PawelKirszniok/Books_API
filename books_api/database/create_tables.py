from books_api.database.database_service import DatabaseService, Base


def create_tables():
    """this function will not be run automatically. Run the file to create all of the required tables"""

    database_service = DatabaseService()

    Base.metadata.create_all(bind=database_service.engine)


if __name__ == "__main__":
    create_tables()