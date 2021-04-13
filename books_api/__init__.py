from books_api.database.database_service import DatabaseService
from books_api.external_api_service import ExternalApiService
from books_api.api import app

database_service = DatabaseService()
google_api_service = ExternalApiService()
application = app
