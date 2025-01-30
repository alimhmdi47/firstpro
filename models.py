from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
#from sqlalchemy_utils import EmailType, PasswordType, URLType
from datetime import datetime
from pydantic.networks import EmailStr
from typing import List, Optional


class Usertype (str, Enum):
    admin = "admin"
    author = "author"
    customer = "customer"

class SubscriptionModels(int, Enum):
    free = 0
    plus = 1
    premium = 2

############# CITY
class City(SQLModel,table=True):
    __tablename__ = "city"
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False, unique=True)

############## GENRE
class Genre(SQLModel,table=True):
    __tablename__ = "genre"
    id: Optional[int] = Field(primary_key=True,default=None)
    name: str = Field(nullable=False, unique=True)

    books: List["Book"] = Relationship(back_populates="genre")


# ############# BOOKAUTHOR
class BookAuthor(SQLModel, table=True):
     __tablename__ = "bookauthor"
     book_id : int = Field(foreign_key="book.id",primary_key=True)
     author_id : int = Field(foreign_key="author.user_id",primary_key=True)

     author : "Author" = Relationship()
     book : "Book" = Relationship()


########### SUBSCRIPTION
class Subscription(SQLModel ,table=True):
    __tablename__ = "subscription"
    cus_id:int = Field(foreign_key="customer.user_id", primary_key=True)
    sub_start : datetime = Field(nullable=False)
    sub_end :datetime =Field(default=datetime.now,nullable=False)

    cus : "Customer" = Relationship(back_populates="sub")

    class Config:
        arbitrary_types_allowed = True

############## CUTOMER
class Customer(SQLModel ,table=True):
    __tablename__ = "customer"
    user_id:int = Field(foreign_key="user.id", primary_key=True)
    sub_model : SubscriptionModels = Field(nullable=False)
    wal_amo : int = Field(default=0,nullable=False)

    user : "User" = Relationship()
    sub : "Subscription" = Relationship(back_populates="cus")

    class Config:
        arbitrary_types_allowed = True


################ BOOK
class BookProperty(SQLModel):
    title: str = Field(nullable=False)
    isbn: str = Field(nullable=False, unique=True)
    price: int = Field(nullable=False)
    units: int = Field(default=0, nullable=False)
    description: str = Field(nullable=False)

    class Config:
         arbitrary_types_allowed = True

class Bookcreate(BookProperty):
    genre : str = Field(nullable=False)
    # authorsofbook : Optional[list[str]]


class Book(BookProperty, table=True):
    __tablename__ = "book"
    id: Optional[int] = Field(primary_key=True,default=None)
    created_time: datetime = Field(default_factory=datetime.now)
    genre_id : Optional[int] = Field(foreign_key="genre.id", ondelete="CASCADE", default=None)
    genre: "Genre" = Relationship(back_populates="books")
    authors: list["Author"] = Relationship(back_populates="books", link_model=BookAuthor)



########### AUTHOR
class Author(SQLModel,table=True):
    __tablename__ = "author"
    id : Optional[int] = Field(primary_key=True,default=None)
    user_id: int = Field(foreign_key="user.id", unique=True)
    # city_id: Optional[int] = Field(foreign_key="city.id",ondelete="CASCADE", default=None)
    goodreads: Optional[EmailStr] = Field( unique=True,default=None)
    bank_account: Optional[str] = Field( unique=True,default=None)

    books: list["Book"] = Relationship(back_populates="authors", link_model=BookAuthor)
    user : "User" = Relationship()
    # city : "City" = Relationship()

    class Config:
        arbitrary_types_allowed = True



############# USERS
class Userpropety(SQLModel):
    username: str = Field(max_length=50, nullable=False, unique=True)
    flname: str = Field(max_length=50, nullable=False)
    phone_number: str = Field(max_length=11, nullable=False)
    email: EmailStr = Field(max_length=50, nullable=False, unique=True)
    password: str = Field(min_length=8, max_length=50,
                          regex=r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$"
                          , nullable=False)
    role: Usertype = Field(default=Usertype.customer,nullable=False)
    def __str__(self):
        return self.username
    # class Config:
    #     arbitrary_types_allowed = True
class User(Userpropety,table=True):
    __tablename__ = "user"
    id: Optional[int] = Field(primary_key=True, default=None)
    created_time: datetime = Field(default_factory=datetime.now)
