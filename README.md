# firstpro
# Book Manager API
A simple CRUD system with serialization and persistence!

## Description
Book Manager API is a web application that allows users (include Authors and Customers) to manage a collection of books
and reserve.
Authors can register their books and so delete and edit their own books and profile.
Users can create, update, delete, and retrieve books.
There is another person that access to change all data. He is Admin.

## Installation

### Prerequisites:
- Python 3.8+
- PostgreSQL installed and running
- PGAdmin for database management (optional but recommended)

## Models
Tables:
User
Author
Customer
Book
Bookauthor
Subcription
Genre
City

## There are 4 test folder that previous versions in it

### API Endpoints:
- `GET /books/` - Retrieve a list of all books
- `POST /books/register` - Add a new book
- `GET /authors/` - Retrieve authors information
- `POST /users/signup` - Signup users include customers and authors
