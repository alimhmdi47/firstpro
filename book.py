from sqlalchemy.ext.asyncio import AsyncSession

from database import get_session
from models import Book, Bookcreate, Genre, BookAuthor, Author, User
from fastapi import FastAPI, APIRouter, Depends
from sqlmodel import Session, select

router = APIRouter(prefix="/books", tags=["book"])

@router.post("/register")
async def creat_book(bookinfo: Bookcreate , dbsession:AsyncSession=Depends(get_session))-> str | Book:
    statement = select(Genre.id).where(Genre.name == bookinfo.genre)
    booksgenres = await dbsession.execute(statement)
    genre_id = booksgenres.scalar()
    if not genre_id:
        return "errororoororororor"
    book_data = bookinfo.model_dump()
    book_data["genre_id"] = genre_id #plus data
    db_book = Book.model_validate(book_data)
    db_book.genre_id = genre_id
    dbsession.add(db_book)
    await dbsession.commit()
    await dbsession.refresh(db_book)
    return db_book
    # for authori in bookinfo.authorsofbook:
    #     statement = select(User.id).where(User.flname == authori and User.role == "author")
    #     author_id = await dbsession.execute(statement)
    #     db_bookauthor = BookAuthor(book_id = db_book.id, author_id = author_id)
    #     dbsession.add(db_bookauthor)
    #     await dbsession.commit()
    #     await dbsession.refresh(db_bookauthor)

@router.get("/")
async def read_books( dbsession:AsyncSession=Depends(get_session)):

    ######
    statement = select(Book)
    sqlbooks = await dbsession.execute(statement)
    books = sqlbooks.scalars().all()
    # json_books = [row.model_dump() for row in books]
    return books

# @router.put()
# def update_book():
#     pass
#
#
# @router.delete()
# def delete_book():
#     pass