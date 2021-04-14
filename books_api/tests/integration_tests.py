import requests
import logging


def test_endpoint_get_book():
    response = requests.get('http://books_api.pawelkirszniok.com/books/33HUiYwuBxQC')

    correct_response = {
        "title": "The Hobbit and Philosophy",
        "authors": [
            "Gregory Bassham",
            "Eric Bronson"
        ],
        "categories": [
            "Literary Criticism"
        ],
        "published_date": 2012,
        "average_rating": 4.0,
        "ratings_count": 1,
        "thumbnail": "http://books.google.com/books/content?id=33HUiYwuBxQC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
    }

    if correct_response == response.json():
        return True
    else:
        logging.warning(response)
        return False


def test_endpoint_get_books():
    result = True

    response = requests.get('http://books_api.pawelkirszniok.com/books?published_date=2012&author="Paddy Kempshall"').json()

    correct_response = [
        {
            "title": "The Hobbit",
            "authors": [
                "Paddy Kempshall"
            ],
            "categories": [
                "Juvenile Fiction"
            ],
            "published_date": 2012,
            "average_rating": -1.0,
            "ratings_count": 0,
            "thumbnail": "http://books.google.com/books/content?id=Wy0svf_7NzsC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        }
    ]

    if response != correct_response:
        result = False
        logging.warning(response)

    response = requests.get('http://books_api.pawelkirszniok.com/books?sort=-published_date&author="John Ronald Reuel Tolkien"').json()

    correct_response = [
        {
            "title": "The Fellowship of the Ring",
            "authors": [
                "John Ronald Reuel Tolkien",
                "Alan Lee"
            ],
            "categories": [
                "Adventure stories"
            ],
            "published_date": 2008,
            "average_rating": 4.0,
            "ratings_count": 2554,
            "thumbnail": "http://books.google.com/books/content?id=5QRZ4z6A1WwC&printsec=frontcover&img=1&zoom=1&source=gbs_api"
        },
        {
            "title": "The Hobbit, Or There and Back Again",
            "authors": [
                "John Ronald Reuel Tolkien"
            ],
            "categories": [
                "Fantasy fiction"
            ],
            "published_date": 1982,
            "average_rating": 4.5,
            "ratings_count": 88,
            "thumbnail": "http://books.google.com/books/content?id=hFfhrCWiLSMC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        {
            "title": "J. R. R. Tolkien's the Hobbit",
            "authors": [
                "John Ronald Reuel Tolkien",
                "Patricia Gray"
            ],
            "categories": [
                "Dramatization"
            ],
            "published_date": 1967,
            "average_rating": 4.0,
            "ratings_count": 1,
            "thumbnail": "http://books.google.com/books/content?id=6MCbciiEnboC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        },
        {
            "title": "The Hobbit",
            "authors": [
                "John Ronald Reuel Tolkien"
            ],
            "categories": [
                "Baggins, Bilbo (Fictitious character)"
            ],
            "published_date": 1937,
            "average_rating": 4.0,
            "ratings_count": 2534,
            "thumbnail": None
        }
    ]

    if response != correct_response:
        result = False
        logging.warning(response)

    response = requests.get('http://books_api.pawelkirszniok.com/books?author="John Ronald Reuel Tolkien"&author="Patricia Gray"').json()

    correct_response = [
        {
            "title": "J. R. R. Tolkien's the Hobbit",
            "authors": [
                "John Ronald Reuel Tolkien",
                "Patricia Gray"
            ],
            "categories": [
                "Dramatization"
            ],
            "published_date": 1967,
            "average_rating": 4.0,
            "ratings_count": 1,
            "thumbnail": "http://books.google.com/books/content?id=6MCbciiEnboC&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api"
        }
    ]
    if response != correct_response:
        result = False
        logging.warning(response)

    return result


if __name__ == "__main__":
    if test_endpoint_get_book():
        logging.warning("get_book test passed")
    else:
        logging.warning("get_book test failed")

    if test_endpoint_get_books():
        logging.warning("get_books test passed")
    else:
        logging.warning("get_books test failed")
