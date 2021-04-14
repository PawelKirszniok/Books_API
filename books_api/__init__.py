from books_api.database.database_service import DatabaseService

database_service = DatabaseService()

from books_api.external_api_service import ExternalApiService

google_api_service = ExternalApiService()

from books_api.api import app
application = app
