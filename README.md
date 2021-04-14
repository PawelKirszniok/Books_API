# Books_API


## Table of contents

* .[About](#about)
* .[Requirements](#requirements)
* .[Decisions and tradeoffs](#decisions)
* .[Demo](#demo)


## About

a simple API working with https://www.googleapis.com/books/v1 powered by Flask and SQLAlchemy. 

This project was made to outside requirements in a limited time.


## Requirements: 

Create an API based on https://www.googleapis.com/books/v1/volumes?q=Hobbit which will support the following operations

GET /books - list all books and support :
* filtering by published date using the syntax: /books?published_date=1995
* sorting by published date using the syntax: /books?sort=-published_date
* filtering by author with the syntax:  /books?author="Author One"&author="Author Two" 


GET /books/<bookId> - return a single book by bookId

Books are to be returned in the format below: 
~~~
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
}
~~~

POST /db with a body {"q": "war"} - get a new data set matching the query from the source and update the database, overwriting if necessary. 


## Decisions:

A number of business decisions were left up to me so I'd like to discuss the ones that were made and the rationale for each one

### Extensibility 

While all software needs to be as extensible as possible we need to also limi the amount of optimizations which are made purely for the future benefit of the software. Therefore I've identified some directions I'm expecting to expand in the future based on the current use case and I've strived to make those directions as easy as possible with my architecture decisions. Those directions are: 

* adding more filtering terms - since the company already searches by numerous terms its likely that a future requirement for filtering by rating or category might arise. In the selected architecture such a change would only require a single method of the DatabseService class and and an extra variable + if statement to be added to the get_books endpoint.

* combining the filtering options - this was not an explicit requirement but I've been able to provide support for combining any amount of filters and a single sort parameter, treating them as an AND relationship. This makes the module more flexible both currently and if extended with more filtering options. 

* adding/changing supported API's - if the company were to require a different API provider to either complement or replace Google's product such a change could easily be made as the knowledge of API is limited to the ExternalApiService class which exposes a simple interface. 

* changing database solutions - similarly current database could easily be replaced. If the new schema would be compatible with SQLAlchemy a change will most likely only need to be reflected in the database login string used in a single place and loaded from a config file. If not then the changes would be limited to the internals of the DatabaseService class.

#### Author filtering - Is it an OR or an AND operation

I've decided to currently support the AND operation. Therefore when you list multiple authors the results will only include books that are related to every author listed. 

This was an arbitrary business decision since both interpretations are usefull and both could be just as easily implemented.

#### Sorting direction and syntax

In my experence ascending sorting is the default in many applications and as such I've decided to default to sort ascendingly when just 'published_date' is passed. Adding a '-' at the beggining does therefore reverse the direction of sorting. 


## Demo:

The API is hosted on pythonanywhere and available using the URLS below:

~~~
books_api.pawelkirszniok.com/books
books_api.pawelkirszniok.com/books/
books_api.pawelkirszniok.com/db
~~~
