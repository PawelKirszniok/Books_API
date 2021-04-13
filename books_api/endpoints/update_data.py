from flask_restful import Resource
from flask import request
from books_api import database_service, google_api_service


class UpdateData(Resource):
    """Endpoint supporting a POST request that will update the database with current data from the GOOGLE API"""

    def post(self):
        """retrieves the data from Google API and initiates the database update. If q is not found in request nothing
         will be updated"""

        data = request.get_json(force=True, silent=True)
        if 'q' in data:
            query = data['q']
        else:
            return

        google_api_response = google_api_service.get_data(query)

        database_service.update_data(google_api_response)

